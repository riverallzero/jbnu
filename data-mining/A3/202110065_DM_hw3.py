import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import torch
import torch.nn.functional as F


def content_based(train_data, test_data):
    train_genres = train_data['genres'].apply(lambda x: ' '.join(x.split('|'))).tolist()
    test_genres = test_data['genres'].apply(lambda x: ' '.join(x.split('|'))).tolist()

    print('    o computing TF-IDF ...')

    vectorizer = TfidfVectorizer()
    train_tfidf = vectorizer.fit_transform(train_genres)
    test_tfidf = vectorizer.transform(test_genres)

    print('    o computing Cosine Similarity ...')

    similarities = cosine_similarity(test_tfidf, train_tfidf)

    print('    o predicting Test Data ...')

    train_ratings = train_data['rating'].fillna(0).values

    weighted_sum = similarities @ train_ratings  
    similarity_sum = similarities.sum(axis=1)  

    epsilon = 1e-8
    predicted_ratings = weighted_sum / (similarity_sum + epsilon)

    predictions = pd.DataFrame({
        'rId': test_data['rId'].values,
        'rating': predicted_ratings
    })

    return predictions


def collaborative_filtering(train_data, test_data, N):
    print('    o normalizing Train Data ...')

    # # user-user
    # cf_type = train_data.pivot_table('rating', index='userId', columns='movieId').fillna(0)
    # is_item_item = False
    
    # item-item
    cf_type = train_data.pivot_table('rating', index='movieId', columns='userId').fillna(0)
    is_item_item = True

    print(f'    o normalized as {"Item x Item" if is_item_item else "User x User"}')

    row_means = cf_type.apply(lambda row: row[row != 0].mean(), axis=1)

    cf_type_normalized = cf_type.apply(
        lambda row: row.apply(lambda value: value - row_means[row.name] if value != 0 else 0),
        axis=1
    )

    print('    o computing Cosine Similarity ...')

    cosine_sim = cosine_similarity(cf_type_normalized)

    if is_item_item:
        index_map = {movie: idx for idx, movie in enumerate(cf_type.index)}
        user_index_map = {user: idx for idx, user in enumerate(cf_type.columns)}
    else:
        index_map = {user: idx for idx, user in enumerate(cf_type.index)}
        user_index_map = {movie: idx for idx, movie in enumerate(cf_type.columns)}

    print('    o predicting Test Data ...')

    predicted_ratings = []

    for user, movie in zip(test_data['userId'], test_data['movieId']):
        if is_item_item:
            if movie not in index_map or user not in user_index_map:
                predicted_ratings.append(1)
                continue

            movie_idx = index_map[movie]
            user_idx = user_index_map[user]
            similarities = cosine_sim[movie_idx, :]

        else:
            if user not in index_map or movie not in user_index_map:
                predicted_ratings.append(1)
                continue

            user_idx = index_map[user]
            similarities = cosine_sim[user_idx, :]

        top_N_indices = similarities.argsort()[-N:][::-1]

        numerator = np.sum(similarities[top_N_indices] * cf_type.iloc[top_N_indices, user_idx])
        denominator = np.sum(np.abs(similarities[top_N_indices]))

        predicted_rating = numerator / denominator if denominator != 0 else 0
        predicted_ratings.append(predicted_rating)

    predictions = pd.DataFrame({
        'rId': test_data['rId'].values,
        'rating': predicted_ratings
    })

    return predictions


def latent_factor(train_data, test_data):
    print('    o normalizing Train Data ...')

    train_user_map = {user: idx for idx, user in enumerate(train_data['userId'].unique())}
    train_movie_map = {movie: idx for idx, movie in enumerate(train_data['movieId'].unique())}

    train_data['userId'] = train_data['userId'].map(train_user_map)
    train_data['movieId'] = train_data['movieId'].map(train_movie_map)

    test_user_map = {user: idx for idx, user in enumerate(test_data['userId'].unique())}
    test_movie_map = {movie: idx for idx, movie in enumerate(test_data['movieId'].unique())}

    test_data['userId'] = test_data['userId'].map(test_user_map)
    test_data['movieId'] = test_data['movieId'].map(test_movie_map)

    test_items = torch.LongTensor(test_data['movieId'].values)
    test_users = torch.LongTensor(test_data['userId'].values)

    # Item x User Table
    item_user = train_data.pivot_table('rating', index='movieId', columns='userId').fillna(0)

    dataset = item_user.to_numpy()

    # Validation Dataset
    rows, cols = dataset.shape
    val_rows_start = rows // 2
    val_cols_start = cols // 2

    val_dataset = dataset.copy()

    val_dataset_types = [
        [slice(None, val_rows_start), slice(None, val_cols_start)],
        [slice(None, val_rows_start), slice(val_cols_start, None)],
        [slice(val_rows_start, None), slice(None, val_cols_start)],
        [slice(val_rows_start, None), slice(val_cols_start, None)],
    ]

    dtype_preds = []
    for t, dataset_type in enumerate(val_dataset_types):
        train_dataset = dataset.copy()
        train_dataset[dataset_type[0], dataset_type[1]] = 0

        # Bias initialization
        non_zero_values = train_dataset[train_dataset != 0] 
        mu = torch.tensor(non_zero_values.mean(), dtype=torch.float32)

        num_users, num_items = train_dataset.shape[1], train_dataset.shape[0]
        b_i = torch.zeros(num_items, requires_grad=True, dtype=torch.float32)   
        b_x = torch.zeros(num_users, requires_grad=True, dtype=torch.float32) 

        print('    o initializing P, Q ...')

        rank = 10
        P = torch.rand(num_users, rank, requires_grad=True)
        Q = torch.rand(num_items, rank, requires_grad=True)

        print(f'    o training with Dataset {t + 1} ...')

        items = torch.LongTensor(train_data['movieId'].values)
        users = torch.LongTensor(train_data['userId'].values)
        ratings = torch.FloatTensor(train_data['rating'].values)

        # Global effect
        optimizer = torch.optim.SGD([P, Q, b_i, b_x], lr=0.1)  
        lambdas = 2e-05
        epochs = 50000

        train_losses, val_losses = [], []
        for epoch in range(epochs):
            # Train
            train_preds = torch.sum(P[users] * Q[items], dim=1) + mu + b_i[items] + b_x[users] 
            train_loss = torch.sqrt(F.mse_loss(train_preds, ratings)) + lambdas * ((P ** 2).sum() + (Q ** 2).sum() + (b_i ** 2).sum() + (b_x ** 2).sum())  

            optimizer.zero_grad()
            train_loss.backward()
            optimizer.step()

            # Val
            val_true = torch.FloatTensor(val_dataset[dataset_type[0], dataset_type[1]])
            val_mask = val_true != 0
            val_preds = torch.matmul(Q[dataset_type[0]], P[dataset_type[1]].T) + b_i[dataset_type[0]].unsqueeze(1) + b_x[dataset_type[1]] + mu

            val_true_masked = val_true[val_mask]
            val_preds_masked = val_preds.view(-1)[val_mask.view(-1)]

            val_loss = torch.sqrt(F.mse_loss(val_preds_masked, val_true_masked))

            train_losses.append((train_loss.item()))
            val_losses.append((val_loss.item()))

            if (epoch + 1) % 1000 == 0:
                print(
                    f'      - Epoch | {epoch + 1}/{epochs}, train(RMSE+Regularization) | {train_loss.item()}, valid(RMSE) | {val_loss.item()}')

        mean_train_loss = sum(train_losses) / len(train_losses)
        mean_val_loss = sum(val_losses) / len(val_losses)

        print(f'    o Dataset {t + 1} Mean Loss, train | {mean_train_loss}, valid | {mean_val_loss}')

        # Test
        predicted_ratings = (torch.sum(P[test_users] * Q[test_items], dim=1) + mu + b_i[test_items] + b_x[test_users]).detach().numpy()
        dtype_preds.append(predicted_ratings)

        # # Loss Graph
        # plt.figure(figsize=(10, 6))
        # plt.plot(range(1, epochs + 1), train_losses, label='Train Loss', color='blue', marker='o', markersize=1)
        # plt.xlabel('Epoch')
        # plt.ylabel('Train Loss', color='blue')

        # ax2 = plt.gca().twinx()
        # ax2.plot(range(1, epochs + 1), val_losses, label='Validation Loss', color='red', marker='o', markersize=1)
        # ax2.set_ylabel('Validation Loss', color='red')

        # plt.title(f'Latent Factor Model Loss: dtype {t + 1}')
        # plt.tight_layout()
        # plt.savefig(f'./dtype_{t + 1}_loss.png')

    print('    o making Result ...')

    predictions = pd.DataFrame({
        'rId': test_data['rId'].values,
        'rating': sum(dtype_preds)/len(dtype_preds)
    })

    predictions['rating'] = predictions['rating'].apply(lambda val: 1 if val <= 1 else (5 if val > 5 else round(val, 1)))

    return predictions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', default='./jbnu-dm-2024-recommendation/train.csv')
    parser.add_argument('--test', default='./jbnu-dm-2024-recommendation/test.csv')

    args = parser.parse_args()

    train_data = pd.read_csv(args.train)
    test_data = pd.read_csv(args.test)

    df_submission_path = './submission.csv'

    models = {0: 'Content Based', 1: 'Collaborative Filtering', 2: 'Latent Factor'}
    model = int(input('Enter Model Type \n  o content based: 0, collaborative filtering: 1, latent factor: 2 => '))

    assert model in models, 'Invalid Model Type'

    if model == 0:
        drop_list = ['movieId', 'title', 'year']
        train_data.drop(drop_list, axis=1, inplace=True)
        test_data.drop(drop_list, axis=1, inplace=True)

        print(f'  o selected "{models[model]}" model')

        print('\n | Content Based Model')
        predictions = content_based(train_data, test_data)

    elif model == 1:
        drop_list = ['genres', 'year']
        train_data.drop(drop_list, axis=1, inplace=True)
        test_data.drop(drop_list, axis=1, inplace=True)

        print(f'  o selected "{models[model]}" model')

        print('\n | Collaborative Filtering Model')
        predictions = collaborative_filtering(train_data, test_data, N=2)

    else:
        drop_list = ['title', 'genres', 'year']
        train_data.drop(drop_list, axis=1, inplace=True)
        test_data.drop(drop_list, axis=1, inplace=True)

        print(f'  o selected "{models[model]}" model')

        print('\n | Latent Factor Model')
        predictions = latent_factor(train_data, test_data)

    predictions.to_csv(df_submission_path, index=False)
    print(f'  o saved results in "{df_submission_path}"')


if __name__ == '__main__':
    main()
    