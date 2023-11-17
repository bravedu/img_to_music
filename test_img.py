import services.imgToMusic

imgUrl = "https://oss.pengyin.vip/b5b5e36fefee3a93afbf6dc51f6a154ecb8441a06a8c6f541ff115118b88f782.jpg?x-oss-process=image/auto-orient,1/resize,m_lfit,w_200/quality,q_90"
data = services.imgToMusic.ImageUrlToText(imgUrl)
print(data)