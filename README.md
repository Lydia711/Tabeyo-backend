
<p align="center">
  <img src="https://github.com/Lydia711/Tabeyo-frontend/blob/main/src/assets/images/tabeyoLogo.png" style="width:450px;height:300px;">
</p>

## About Tabeyo - Backend

With the abundance of apps made to ease the search of recipes, not many accomodate to the fact that it's difficult to have every ingredient available at hand. Therefore, Tabeyo is focused on finding recipes with only what's available in the fridge/pantry.

Here's why:
* **No grocery store runs required:** Sometimes you don't have the time or resources to make a trip to the grocery store.
* **Resourceful cooking:** You often just want to use what you have as a resourceful adult.
* **Saving expired Ingredients:** You may have ingredients on the brink of expiration that want to use ASAP.

This is the backend portion of Tabeyo, make sure to check out the [README of the frontend](https://github.com/Lydia711/Tabeyo-frontend) portion for the frontend setup.


### Built With

The backend of Tabeyo uses the following Languages/Frameworks/Libraries:

* [Python V3](https://www.python.org/downloads/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Pypi requests](https://pypi.org/project/requests/)


## Getting Started

Tabeyo uses Edamam, a free recipes lookup API. Therefore, to use the app, you will have to get your free Edamam API ID and Key, the following section will guide you through this process.
Here's how to locally setup the backend of Tabeyo:

### Installations

1. Install [Python V3](https://www.python.org/downloads/)
2. Clone the repo
   ```sh
   git clone https://github.com/Lydia711/Tabeyo-backend.git
   ```
3. Get your free Edamam API ID and Key
    - Sign up for a free account at [Edamam](https://developer.edamam.com/edamam-recipe-api)
    - Create a new app and retrieve your 'App ID' and 'App Key'
4. Navigate to the project directory
   ```sh
   cd Tabeyo-backend/app
   ```
5. Create .env file to contain your newly retreived ID and Key
    ```sh
    "# Environment Variables" | Out-File -FilePath .env -Encoding utf8
    "EDAMAM_APP_ID=" | Out-File -FilePath .env -Encoding utf8 -Append
    "EDAMAM_API_KEY=" | Out-File -FilePath .env -Encoding utf8 -Append
     ```
6. Use your favorite editor to add your ID and Key to the .env file
7. Install the requirements (FastAPI, Uvicorn, Pypi requests, dotenv)
   ```sh
   pip install -r requirements.txt
   ```
8. Run the API
   ```sh
   uvicorn main:app
   ```
This will run the app on http://127.0.0.1:8000

## Usage

### Regular Recipe Search

<p align="center">
  <img src="https://github.com/Lydia711/Tabeyo-frontend/blob/main/src/assets/gifs/searchDemo.gif">
</p>

### Strict Recipe Search

<p align="center">
  <img src="https://github.com/Lydia711/Tabeyo-frontend/blob/main/src/assets/gifs/strictSearchDemo.gif">
</p>

## Roadmap

- [ ] Add a limit to missing ingredients for strict search (current is 4 ingredients)
- [ ] 'Search by recipe name' feature

If you have an interesting idea to add, check out the Contributing section below!

## Contributing

If you have any ideas or features to add to the project to improve it, you are more than welcome to contribute!
Make sure to follow the following simple steps to add your own amazing feature to Tabeyo:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Submit a Pull Request

### Top contributors:

Currently, Tabeyo is a solo project by [Lydia Youssef](https://github.com/Lydia711), but additional contributors would be highly appreciated!

## Contact

Lydia Youssef - [LinkedIn](https://www.linkedin.com/in/lydia-youssef-4b5831176/)
<br>
For any questions or recommendations, feel free to discuss it with me on LinkedIn or Github!
<br>
Project Links: [Tabeyo frontend](https://github.com/Lydia711/Tabeyo-frontend) and [Tabeyo backend](https://github.com/Lydia711/Tabeyo-backend)


## Acknowledgments

I must give credit to the following resources since they were quite helpful in the development of this project:

* [Edamam API](https://developer.edamam.com/edamam-recipe-api) - Free, powerful API for recipes and ingredients data
