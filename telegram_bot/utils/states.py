from aiogram.fsm.state import State, StatesGroup


class AuthFSM(StatesGroup):
    login_email = State()
    login_password = State()
    reg_first = State()
    reg_last = State()
    reg_email = State()
    reg_password = State()
    reg_password2 = State()


class LearnFSM(StatesGroup):
    sql = State()
    homework_file = State()
    support = State()
    teacher_pick_student = State()
    teacher_msg = State()
    announce_title = State()
    announce_body = State()
    review_score = State()
    review_feedback = State()
    excel_note = State()
