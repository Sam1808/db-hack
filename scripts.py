import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation

def get_schoolkid_account(kid_name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=kid_name).get()
        return schoolkid
    except ObjectDoesNotExist:
        print(f'Не могу найти ученика по имени {kid_name}')
        return None
    except MultipleObjectsReturned:
        print(f'Слишком много учеников с именем {kid_name}. Детализируй!')
        return None

def fix_marks(kid_name):
    schoolkid = get_schoolkid_account(kid_name)
    if not schoolkid:
        return None
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for mark in schoolkid_bad_marks:
        mark.points = 5
        mark.save()

def remove_chastisements(kid_name):
    schoolkid = get_schoolkid_account(kid_name)
    if not schoolkid:
        return None
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in schoolkid_chastisements:
        chastisement.delete()

def create_commendation(kid_name, subject_of_lesson):
    schoolkid = get_schoolkid_account(kid_name)
    if not schoolkid:
        return None
    schoolkid_lessons = Lesson.objects.filter(group_letter=schoolkid.group_letter, year_of_study=schoolkid.year_of_study)
    subject_schoolkid_lessons = schoolkid_lessons.filter(subject__title=subject_of_lesson).order_by('date').reverse()
    last_lesson = subject_schoolkid_lessons[0]
    wishes = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
            'Великолепно!', 'Прекрасно!','Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
            'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!','Талантливо!',
            'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
            'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
            'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
            'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
            'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']
    Commendation.objects.create(
            text=random.choice(wishes),created=last_lesson.date,schoolkid=schoolkid,subject=last_lesson.subject,teacher=last_lesson.teacher
        )

print('Scripts READY ! ')