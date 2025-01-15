# Poparide take-home project

This project is used by Poparide to assess your technical skills and way of thinking as they pertain to our Product team. We've created a base template for you to work from with the intention of providing a bit of structure, and to save you time fiddling around with setup and config. You can change anything you like, but please stick with [Django Rest Framework](https://www.django-rest-framework.org/).

## Instructions
To get started, **create a new repository from this template**. Please make your copy *private*. You should have received a list Github accounts belonging to your reviewers. Once ready, please invite them to collaborate so they can review your project.


---

## The project
Your task is to create an API endpoint for users to request a ride on a `Trip`.

The project simulates a carpool service where users can:
- Post a `trip` as a **driver**.
- Request a ride as a **passenger**.

We've created a basic `Trip` model and endpoint for listing trips as a starting point, but feel free to modify them as you see fit.

### Scope
- *Don't* worry about creating a frontend, or adding functionality to the Trip endpoint itself, unless you feel it's necessary to your design (or you really want to :sweat_smile:).
- *Do* consider how to model a passenger on a trip, and how it would affect trip state.

## How we'll evaluate your work
We'll use this project as the basis for our assessment of your coding skill as it relates to our team. We'll be looking for the following:
- **Design**: How did you model the problem at hand? Is it maintainable & extendible? Have you thought about how it will change in the future?
- **Code quality**: Is your code clean, modular, & secure? Have you made appropriate use of the language/framework? Is your API consistent and adherent to REST principles?
- **Testing**: Have you considered how you'd test your code?
- **Documentation**: Did you provide context around your decisions and assumptions? Is the scope of the work clearly defined? (Please use the **Notes** Section below!)

### Time expecations
We respect your time and don't expect you to spend more than **2 hours** on this task, and time spent is not a criterion for our assessment. That being said, if you choose to spend significantly more (or less) time on it, please indicate that in the **Notes** section below, and we'll keep that in mind when evaluating the project.

We encourage you to use the Notes section to tell us what you would have done differently given more time, things that were out of scope, etc. We don't expect a finished product in 2 hours - more important are the foundations and your thought process behind it!

### A note on AI
We encourage you to make use of tools like ChatGPT as you would in your regular job. However, please keep in mind that we value **clean, cohesive, and thoughtful design** over quantity.


---

## Project setup
To set up the project locally, follow these steps:

1. Install Python (suggested: use [pyenv](https://github.com/pyenv/pyenv) with Python 3.12).
2. Install Django & DRF:
    ```bash
    python -m pip install -r requirements.txt
    ```
3. Run the migrations:
    ```bash
    cd carpool
    python manage.py migrate
    ```
4. (Optional) Load sample data:
    ```bash
    python manage.py loaddata fixtures/users.json fixtures/locations.json fixtures/trips.json
    ```

To run the server locally:

```bash
python manage.py runserver
```

To test:

```bash
python manage.py test
```

---

## Notes

Your notes here :eyes:
