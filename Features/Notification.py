# from notifypy import Notify

# notification = Notify(
#   default_notification_title="Initializing...",
#   default_application_name="C.H.E.T.A.N.A",
#   default_notification_icon="E:\\Khilesh AI\\icons\\chetana2.ico",
# #   default_notification_audio="path/to/sound.wav"
# )

# def chetana_online_notify():
#   # stuff happening here.
#   notification.message = "C.H.E.T.A.N.A is Online 🌐"
#   notification.send()
# if __name__ == '__main__':
#     chetana_online_notify()
    
from winotify import Notification,audio

def show_notification(message="C.H.E.T.A.N.A is Online 🌐"):
    toast = Notification(app_id = "C.H.E.T.A.N.A",
                    title = "⚠️Alert⚠️",
                    msg = message,
                    icon = r"E:\Chetana_Final\Stuff\chetana2.ico")
    toast.set_audio(audio.Mail, loop=False)
    toast.show()

if __name__ == "__main__" :
    show_notification()