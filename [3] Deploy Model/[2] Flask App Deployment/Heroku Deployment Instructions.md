# Heroku Deployment Instructions

To deploy the `flask_app` subfolder onto Heroku via the command line, please follow these steps:

1. Create an app on the Heroku website - this is relatively simple to do

2. Login to Heroku via the command line by executing:

   ```bash
   heroku login

3. Next, execute:

   ```bash
   heroku git:remote -a bert-readability-mabilton
   ```

   Note that `bert-readability-mabilton` is the name of the Heroku app we created in Step 1 - replace this string with the name you gave to your Heroku app in Step 1.

4. Assuming we're inside the **root directory** of the `msa-2021-dsproj-mabilton` Git repository, we can then execute:

   ```bash
   git subtree push --prefix '[3] Deploy Model/[2] Flask App Deployment/flask_app' heroku master
   ```

5. After this, we can finally start our Heroku app by executing:

       ```bash
       heroku open
       ```