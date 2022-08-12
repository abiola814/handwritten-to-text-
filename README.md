# handwritten-to-text python web application 

## setup an environment 
```
python3 -m venv venv
```
## installation
To the install the dependencies requirements.txt is created
  ```
  pip3 install -r requirements.txt
  ```
              or
```
  pip install -r requirements.txt
```

## cloud setup
azure was used to host the machine learning algorithm. steps needed
- create azure account
- create a custom vision api enpoint
- deploy train and test with your machine model script
- insert the endpoint and api key to the view.py found in timiocr folder

## configure git on virtual environment
```
git config --global user.name "Your Name"
git config --global user.email "you@youraddress.com"
git config --global push.default matching
git config --global alias.co checkout
git init
```

## deploy to heroku
- create heroku account
- download heroku cli tool
- enter the following command to deploy the application
```
  heroku login
  heroku create 'name of your website'
  git add .
  git commit ' deploy to heroku'
  git push heroku master
```
