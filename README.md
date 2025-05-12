# Events Manager
I have developed APIs to manage events, which could be helpful for knowing in advance which roads are closed on specific dates and times. Users are notified through email subscription.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Techologies](#technologies)
- [Contributing](#contributing)
- [License](#license)


## Installation
1. Clone the repository:
   ```git clone https://github.com/SamantaMancini/web_events_manager.git```

2. Navigate to the project directory:
    ```cd web_events_manager```

3. Install dependencies:
    ```pip install -r requirements.txt```

## Usage
Rename `.envexample` to `.env` and add the required data.
To run the backend APIs, execute this command: <br/> ```fastapi dev main.py``` and click the link ```http://127.0.0.1:8000/docs```
Endpoints:
- POST /events/: Create events endpoint
- GET /events/: Read events endpoint
- GET /events/{event_id}: Read event endpoint 
- PUT /events/{event_id}: Update event endpoint
- DELETE /events/{event_id}: Delete event endpoint

If a specific event is searched for, the user is automatically sent an email with all available events for that date.

## Features
[ ] Send emails once a day to avoid spam. <br/>
[ ] Add a history send emails.

## Technologies
- Python3
- SqlAlchemy
- Sqlite
- Fastapi
- Pytest
- Dotenv

## Contributing
I welcome any feedback for this project to improve it.

## License
This project is licensed under the MIT License - see the `[LICENSE](https://github.com/SamantaMancini/LICENSE)` file for details.


