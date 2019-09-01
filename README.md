# Shop-Scrape

Shop-Scrape is an e-Commerce web scraping platform. It notifies you when your product falls below your specifed price (Removes the need of you having to constantly open the website and check the price).  

## Installation

```bash
git clone https://github.com/shradhasehgal/Shop-Scrape
cd Shop-Scrape
pip install -r requirements.txt
```
Create a file named file.py and add the following variables to it 

```
MY_ADDRESS = "INSERT YOUR OUTLOOK EMAIL-ID HERE"
PASSWORD = "INSERT YOUR PASSWORD HERE"
```

Run the app with the command `python3 app.py`


## How to use?

1. Enter the name of the product, the price below which you are willing to buy it, and your email address.
2. The app returns an e-Commerce website link for the product - if that is what you wanted, proceed by clicking `Yes` or provide the link yourself.
3. The app will send you an email notification when the product falls below the stipulated price. 

**Note** : The app only sends a notification *once* and deletes your entry from the database so you don't have to worry about spam.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) for details.
