import scrapy

# data yang akan diambil
#     nama
#     dept
#     sinta_id
#     Scopus H-index
#     GS H-index
#     SINTA Score 3Yr
#     SINTA Score 
#     Affil Score 3Yr
#     Affil Score

        

               



# data yang akan diambil
#   subject
#   
#   

# nama       
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.profile-name > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.profile-name > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(6) > div > div.col-lg > div.profile-name > a

# dept
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a

# sinta_id
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id

# scopus_h_index
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-warning

# gs_h_index
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-success.ml-3

# sinta_3yr_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(1) > div.stat-num.text-center

# sinta_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(2) > div.stat-num.text-center

# affil_3yr_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(3) > div.stat-num.text-center

# affil_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(4) > div.stat-num.text-center

# image
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg-2 > img