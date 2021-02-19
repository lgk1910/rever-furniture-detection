# rever-furniture-detection API
## Running app.py (Server)
```
python app.py
```
## Running test.py (For testing)
Example:
```
python request.py
URLs (seperated by comma): https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2019/7/16/0/DOTY2019_Connie-Vernich_City-Cottage_5.jpg.rend.hgtvcom.616.411.suffix/1563296826167.jpeg, https://www.thespruce.com/thmb/WEst9BHwmGGE6AtmKrE5ck4m3t4=/3232x2424/smart/filters:no_upscale()/how-to-arrange-living-room-furniture-1976578-hero-c99074dcad854b669b91652046a39203.jpg, https://jumanji.livspace-cdn.com/magazine/wp-content/uploads/2019/09/16191216/Contemporary-Living-Room-Easy-Functionality.jpg
```
## APIs
Current address: **http://127.0.0.1:5000/predict/**

Body of the request and response are both in JSON format.

Example (calling the API with 3 images for prediction):

![Request](https://2.pik.vn/20210f3cf416-b74d-4a3c-b548-9b539834372c.png)
