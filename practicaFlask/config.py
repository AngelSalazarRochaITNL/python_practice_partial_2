class BasicConfig:
        
    USER_DB='postgres'
    PASS_DB='Yon1thek1'
    URL_DB='localhost'
    NAME_DB='eval_emp_flask'
    FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

    SQLALCHEMY_DATABASE_URI= FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICARTIONS = False
    SECRET_KEY="llave_secreta"