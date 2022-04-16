# Extract Transform and Load using multiprocessing.
Here we are extracting files from a database transforming its values and then loading the transformed values into another database using different methods.
such as using a single process for ETL , using Extract Transform and load as 3 different processes, as Transform is time taking using different number of processes for Transform.

INPUT:

<img width="405" alt="Screenshot 2022-04-16 at 10 53 40 PM" src="https://user-images.githubusercontent.com/60423130/163685130-d4096239-08a9-4a3b-aa99-7d96ff77f765.png">

OUTPUT:(after transformation):

<img width="405" alt="Screenshot 2022-04-16 at 10 51 48 PM" src="https://user-images.githubusercontent.com/60423130/163685149-bf22b88d-101a-4095-9cfa-d42ae5687faa.png">

Note these data are for 10Crore entries.
# First we use the normal sequential method of ETL using a single process. results:
<img width="641" alt="Direct_graph" src="https://user-images.githubusercontent.com/60423130/163684593-28c255f0-ab0f-43ab-b69a-4b65fb187421.png">

This is very tedious and time taking 

# Using ETL as different processes:
<img width="641" alt="multiprocessing(1)" src="https://user-images.githubusercontent.com/60423130/163684757-7d9c509d-89ea-4fc9-acf8-8d2e8e12737c.png">

The time taken is reduced tremendously

# Using different number of processes for transforming:
2 processes:

<img width="641" alt="multiprocessing" src="https://user-images.githubusercontent.com/60423130/163684772-79cc6804-8a8c-4373-8bfe-0ddea2a3d2db.png">

we can see 10% improvement from 1 process

3 processes:

<img width="641" alt="Multiprocessing(3)" src="https://user-images.githubusercontent.com/60423130/163684808-075cd280-53c7-41b5-80b5-5f8ebb48a432.png">

We can see not much improvement, this is due to the loading process limiting the speed.






