# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-five-star-sellers

"""

def seller_percentage(productRatings):
    total = 0
    for ratings in range(len(productRatings)):
        total += productRatings[ratings][0]/productRatings[ratings][1]
            
    seller_pct = total/len(productRatings)
    return round(seller_pct * 100 , 2)


def fiveStartReviews(productRatings, ratingsThreshold):
    count = 0
    
    # Percentage
    seller_pct = seller_percentage(productRatings)
    if seller_pct >= ratingsThreshold:
        return count
      
      
    while seller_pct < ratingsThreshold:
        for ratings in range(len(productRatings)):
            if productRatings[ratings][0] != productRatings[ratings][1]:
                productRatings[ratings][0] += 1
                productRatings[ratings][1] += 1 
                seller_pct = seller_percentage(productRatings)
                count += 1
                if seller_pct >= ratingsThreshold:
                    break
        
    return count
    
productRatings = [[4,4], [1,2], [3, 6]]
threshold = 77
print(fiveStartReviews(productRatings, threshold))


# =============================================================================
# def seller_percentage(productRatings):
#     total = 0
#     for ratings in range(len(productRatings)):
#         total += productRatings[ratings][0]/productRatings[ratings][1]
#             
#     seller_pct = total/len(productRatings)
#     return round(seller_pct * 100 , 2)
# 
# 
# def fiveStartReviews(productRatings, ratingsThreshold):
#     count = 0
#     for ratings in range(len(productRatings)):
#             seller_pct = seller_percentage(productRatings)
#             if seller_pct >= ratingsThreshold:
#                     return count
#             else:
#     
#                 while True:
#                     if productRatings[ratings][0] != productRatings[ratings][1]:
#                         productRatings[ratings][0] += 1
#                         productRatings[ratings][1] += 1
#                         seller_pct = seller_percentage(productRatings)
#                         count += 1
#                         if seller_pct >= ratingsThreshold:
#                             break 
#                 if seller_pct >= ratingsThreshold:
#                     break          
#     
#     return count
# =============================================================================

# =============================================================================
# def fiveStartReviews(productRatings, ratingsThreshold):
#     count = 0
#     while True:
#         
#         for ratings in range(len(productRatings)):
#             seller_pct = seller_percentage(productRatings)
#             if seller_pct >= ratingsThreshold:
#                     break 
#             else:    
#                 if productRatings[ratings][0] != productRatings[ratings][1]:
#                     productRatings[ratings][0] += 1
#                     productRatings[ratings][1] += 1
#                     seller_pct = seller_percentage(productRatings)
#                     count += 1
#                     if seller_pct >= ratingsThreshold:
#                         break 
#         if seller_pct >= ratingsThreshold:
#             break          
#     
#     return count
# =============================================================================



            
            