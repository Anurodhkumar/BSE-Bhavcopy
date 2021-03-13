# BSE-Bhavcopy-
1. We need to start a redis server.
2. We have to run the manage.py file of django using python manage.py runserver to start the django server.
3. Bse_Bhavcopy is the project name and stocks is the app name.
4. csv_data_update is the scheduler folder which is using the method csv_data to run every 6pm and update data to redis.
5. apscheduler is used to schedult the redis data every 6pm and we can install it by using pip install apscheduler django psycopg2 requests command.
6. I have added a Table Picture as Output.Png
