import numpy as np

def calculate_cosine_similarity(vec1, vec2):
    """
    計算兩個向量之間的餘弦相似度。

    Args:
        vec1 (list or np.array): 第一個向量。
        vec2 (list or np.array): 第二個向量。

    Returns:
        float: 兩個向量之間的餘弦相似度。
               如果任一向量為零向量，則返回 0.0。

    Raises:
        ValueError: 如果兩個向量的維度不一致。
    """
    if len(vec1) != len(vec2):
        raise ValueError("兩個向量的維度必須一致。")

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

if __name__ == "__main__":
    # 範例用法
    vector_a = [1, 1, 0, 1, 0, 1, 0, 0, 1]
    vector_b = [0, 1, 1, 0, 1, 1, 0, 0, 1]
    vector_c = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    vector_d = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    print(f"向量 A: {vector_a}")
    print(f"向量 B: {vector_b}")
    print(f"向量 C: {vector_c}")
    print(f"向量 D: {vector_d}")
    print("-" * 30)

    similarity_ab = calculate_cosine_similarity(vector_a, vector_b)
    print(f"向量 A 和 向量 B 的餘弦相似度: {similarity_ab:.4f}")

    similarity_ac = calculate_cosine_similarity(vector_a, vector_c)
    print(f"向量 A 和 向量 C 的餘弦相似度: {similarity_ac:.4f}")

    similarity_ad = calculate_cosine_similarity(vector_a, vector_d)
    print(f"向量 A 和 向量 D 的餘弦相似度: {similarity_ad:.4f}")

    try:
        calculate_cosine_similarity([1, 2], [1, 2, 3])
    except ValueError as e:
        print(f"\n錯誤範例 (維度不符): {e}")
