PROJECT VDMap

Requirements
- python\>=3.8

Installation
- create `.env` file
    - required params
    - `DATABASE` - database url
    - `SECRET_KEY` - Flask app secret key
    - possible params
    - `HOST`
    - `PORT`
    - `DEV`

    ````
    pip intsall -r requirements.txt
    ````
To generate admin auth run `flask shell` `p.generate_admin(login, password)` with your login and password and add result output to `ADMIN_AUTH={output}` to `.env`

Run
- `python main.py`