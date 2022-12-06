# Dash_Template_App
Dash Plotly Template App

# Heroku creeate app
heroku create my-dash-app   # change my-dash-app to a unique name
git add .                   # add all files to git
git commit -m 'Initial app boilerplate'
git push heroku master      # deploy code to heroku
heroku ps:scale web=1       # run the app with a 1 heroku "dyno"
