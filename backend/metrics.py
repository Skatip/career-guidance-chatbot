
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_similarity(query_embedding, retrieved_embedding):
    return cosine_similarity([query_embedding], [retrieved_embedding])[0][0]

def rouge_l(prediction, reference):
    pred_tokens = prediction.split()
    ref_tokens = reference.split()
    lcs = _lcs(pred_tokens, ref_tokens)
    return (2 * lcs) / (len(pred_tokens) + len(ref_tokens))

def _lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]
