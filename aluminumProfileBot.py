from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# Bot resposável por realizar uma raspagem de dados no Poliformas - perfis de aluminio:

class Aluminum():
    def __init__(self):
		# Configuração para executar em 2º plano:
        self.options = Options()
        
        self.options.add_argument("--headless")
        self.nav = webdriver.Firefox(options = self.options)
        
        for index in range(1, 2):
			# Acessando a URL:
            self.url = f"https://www.poliformas.com.br/categoria-produto/perfis-de-aluminio/page/{index}/"
            self.nav.get(self.url)
            sleep(5)
            print(f"Acessando URL: {self.url}")
            self.get_title_card()
        return self.title_list
    
    
    # Método responsável por obter o titulo dos perfis:
    def get_title_card(self):
        count = 1
        self.title_list = list()
        while True:
            try:	
                self.xpath_title = f'//*[@id="archive-product"]/div[2]/div[1]/div[2]/div/div[{count}]/div[1]/div[2]/a'
                title = self.nav.find_element(By.XPATH, self.xpath_title)
                title_format = title.text
                print(title_format)
                self.title_list.append(title_format)
                count += 1
            except:
                print('erro - saída')
                break

if __name__ == "__main__":
	aluminio = Aluminum()
	print("========== RESULTADO ==========")
	print(aluminio)
















    # Método responsável por receber o titulo obtido e buscar a imagem:
    #def get_image_by_title(title):[
        #url_img = f'https://www.poliformas.com.br/wp-content/uploads/2019/06/{title}.jpg'
