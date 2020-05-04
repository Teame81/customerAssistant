import datetime
from dbModel import Chat_session, Chat_history, sessionmaker, engine ,datetime

Session = sessionmaker(bind=engine)
Session = Session()
current_chat_hist = Chat_history(message = "Testar", time_stamp = datetime.datetime.utcnow())
current_chat_sess = Chat_session(client_name = "Timmie", operator_name = "Lollo", chat_hist = current_chat_hist)