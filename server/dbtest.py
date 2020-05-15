from dbModel import Chat_session, Chat_history, sessionmaker, engine ,datetime


#Starting a session to DB and start Chat_Session   
Session = sessionmaker(bind=engine)
ThisSession = Session()
    
# current_chat_hist = [Chat_history(message = "Hamster777", time_stamp = datetime.datetime.utcnow())]
# current_chat_sess = Chat_session(client_name = "Lollo123", operator_name = "Operator456", chat_hist = current_chat_hist)
# 
# ThisSession.add(current_chat_sess)
# ThisSession.commit()

findCurrentChatSession = ThisSession.query(Chat_session).filter_by(client_name = "Lollo").first()

findCurrentChatSession.chat_hist = [Chat_history(message = "Meddelande3!", time_stamp = datetime.datetime.utcnow())]

ThisSession.add(findCurrentChatSession)
ThisSession.commit()