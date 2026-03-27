def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    relevant_k  = len(relevant)
    recommended = set(recommended[:k])
    relevant = set(relevant)

    numerator = len(relevant.intersection(recommended))
    
    precision = numerator/k
    recall = numerator/relevant_k

    return [precision,recall]