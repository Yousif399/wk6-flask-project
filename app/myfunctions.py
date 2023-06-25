# functions useful for different back-end/front-end purposes

import requests

# there are 839 different products in the api catalog
class Amiibo():
    """
    Help: instanciate class with a product number arg between 1-839. 
    Use methods: get_id, name, game_series, video_game, img_url, release [US release date] to return information about the product.
    """
    url = "https://www.amiiboapi.com/api/amiibo/"    

    def __init__(self, iteration):
        self.iter = iteration - 1

    def dateTransform(self, string):
        months = {"01": "january", "02": "february", "03": "march", "04": "april", "05": "may" , "06": "june", "07": "july", "08": "august", "09": "september", "10": "october", "11": "november", "12": "december"}
        date = string.split("-")
        year = date[0]
        month = [v for k,v in months.items() if k == date[1]][0]
        day = date[2]
        return " ".join([day, month.title(), year])

    def request_data(self):
        """
        returns amiibos in list of 839 objects
        """
        response = requests.get(self.url)
        data = response.json()
        if not response.ok:
            print("error fetching url")
        data = data["amiibo"][self.iter]
        return data
    
    def get_id(self):
        data = self.request_data()
        amiibo_id = data["tail"]
        return amiibo_id

    def name(self):
        data = self.request_data()
        amiibo_name = data["name"]
        return amiibo_name

    def game_series(self):
        data = self.request_data()
        amiibo_game_series = data["gameSeries"]
        return amiibo_game_series

    def video_game(self):
        data = self.request_data()
        amiibo_video_game = data["amiiboSeries"]
        return amiibo_video_game

    def img_url(self):
        data = self.request_data()
        amiibo_image = data["image"]
        return amiibo_image

    def release(self):
        data = self.request_data()
        amiibo_release_date_US = data["release"]["na"]
        amiibo_release_date = self.dateTransform(amiibo_release_date_US)
        return amiibo_release_date
        
    def details(self):
        det_dict = {}
        det_dict["id"] = self.get_id()
        det_dict["name"] = self.name()
        det_dict["game_series"] = self.game_series()
        det_dict["video_game"] = self.video_game()
        det_dict["img_url"] = self.img_url()
        det_dict["release"] = self.release()
        return det_dict

    
### examples of pulling info with the Amiibo class
### first product
# product1 = Amiibo(1)
# print(product1.details())

### last product
# product839 = Amiibo(839)
# print(product839.release())



