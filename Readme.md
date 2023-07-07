## How to start.
- Install the dependencies with pip install -r requirements.txt
- Start the django project with the command  "python .\manage.py runserver"
- Make sure the project is mounted on the port :8000, or else you will need to adjust the BASE_URL in the main.py file outside of the django project.

## What was made to make the code maintainable?

- All calls to the image source has been put into a service called FrameXService so all the logic concerning comunication with the external service is located in one place.
- Created an interface called ImageSourceService that all Services that want to serve the images for the bot must implement, that way we can make sure, even if we change the image source the bot will still function properly since the revlevant methods will need to be implemented.
- Create a serializer for the Video model that FrameXService returns so I can easily seriealize it and deserialize it when needed.
- Separate the business logic in their own service (FindTheFrameService) so the views will be cleaner and we wll have a separation of concerns between the views that will handle the incoming requests and the services that will handle the business logic.
- In FrameXService, the base url was separated as constant in order to easily replace it if the service change it's domain.
