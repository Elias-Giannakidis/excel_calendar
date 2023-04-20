

class Person:
    def __init__(self, name, constrains, lastWeek, weekend):
        self.name = name
        self.constrains = constrains
        self.calendar = []
        self.initCalendar = []
        self.lastWeek = lastWeek
        self.weekend = weekend

    def printMe(self):
        print('name = ', self.name)
        print('constrains = ', self.constrains)
        print('last week = ', self.lastWeek)
        print('weekend = ', self.weekend)
        print('calendar = ', self.calendar)
        print('-------------------------------------')

    def getScore(self, calendar):
        score = 0
        # 6days seri -1000 #5days seri -500
        # score = score + self.get6DaysSeriScore(calendar)
        #  weekend +40
        score = score + self.weekendPlus(calendar)
        # # repo seri  1 repo + 10, 2 repo + 15, 3 repo + 17
        # score = score + self.getRepoSeriScore(calendar)
        # # evening to morning -10
        # # score = score + self.getScoreEveningToMorning(calendar)
        # # constrains -100
        score = score + self.getConstrainsScore(calendar)
        # # change the current program. +200
        score = score + self.getScoreProgramm(calendar)
        # Repo Balance: score = -repo! - weight/3 * repo where weight = 7 - 6 - 5 ....
        score = score + self.repoBalanceScore(calendar)
        return score

    def getScoreProgramm(self, calendar):
        score = 0
        count = 0
        for day in calendar:
            if(self.calendar[count]['value'] == day):
                score = score + 200
            count = count + 1
        return score

    def getScoreEveningToMorning(self, calendar):
        lastDay = 'repo'
        score = 0
        for day in calendar:
            if(lastDay == 'evening' and day == 'morning'):
                score = score - 10
            lastDay = day
        return score

    # I have to see it again
    def getRepoSeriScore(self, calendar):
        lastDayRepo = False
        twoDaysSeri = False
        score = 0
        repo = 0
        for day in calendar:
            if(day == 'repo' and lastDayRepo):
                repo = repo + 1
                score = score - repo
                twoDaysSeri = True
                lastDayRepo = False
            else:
                if( day == 'repo' and not lastDayRepo):
                    repo = repo + 1
                    score = score - repo
                    lastDayRepo = True
            if(day != 'repo'):
                lastDayRepo = False
        if twoDaysSeri:
            score = score + 10
        return score

    def repoBalanceScore(self, calendar):
        repo = 0
        score = 0
        weight = 0
        for day in calendar:
            if(day == 'repo'):
                repo = repo + 1
                score = score - repo - (weight/3)*repo
                weight = 7
            else:
                weight = weight - 1
        return score

    def getConstrainsScore(self, calendar):
        score = 0
        count = 0
        for day in calendar:
            weekday = self.calendar[count]['weekday']
            if weekday in self.constrains:
                constrain = self.constrains[weekday]
            else:
                if 'Everyday' in self.constrains:
                    constrain = self.constrains['Everyday']
                else:
                    constrain = 'all'
            if (constrain != 'all') and (constrain != day):
                score = score - 100
            count = count + 1
        return score


    def get6DaysSeriScore(self, calendar):
        seri = 0
        score = 0
        for day in calendar:
            if(day == 'repo'):
                seri = 0
            else:
                seri = seri + 1
        if(seri > 5):
            score = score - 500
        if(seri > 6):
            score = score - 1000
        return score

    def weekendPlus(self, calendar):
        weekend = False
        seriWeedays = False
        count = 0
        for day in calendar:
            weekday = self.calendar[count]['weekday']
            if(day == 'repo' and (weekday == 'Saturday' or weekday == 'Sunday')):
                if(seriWeedays):
                    weekend = True
                else:
                    seriWeedays = True
            else:
                seriWeedays = False
            count = count + 1
        score = 0
        if(weekend):
            score = 40
        return score

    def getValidWorkDay(self, day):
        if day in self.constrains:
            return self.constrains[day]
        if (self.constrains['everyday']):
            return self.constrains['everyday']

    def canWorkTomorrow(self):
        count = 0
        revCalendar = self.calendar.copy()
        revCalendar.reverse()
        revLastWeek = self.lastWeek.copy()
        revLastWeek.reverse()
        while True:
            for day in revCalendar:
                if (count >= 6):
                    return {"days": count, "canWork": False}
                    break
                if (day == 'repo'):
                    return {"days": count, "canWork": True}
                    break
                count = count + 1
            for day in revLastWeek:
                if (count >= 6):
                    return {"days": count, "canWork": False}
                    break
                if (day == 'repo'):
                    return {"days": count, "canWork": True}
                    break
                count = count + 1

# From staff_people get the people. It is un-efficient but who cares?
def genPeople(staff_people):
    const_keys = ['Everyday', 'Monday', 'Tuesday', 'wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    people = []
    for staff_person in staff_people:
        if "Name" in staff_person:
            newConstrains = {}
            for key in const_keys:
                if key in staff_person:
                    newConstrains[key] = staff_person[key]
            if 'weekend this month' in staff_person:
                newWeekend = staff_person['weekend this month'] == 'yes'
            else:
                newWeekend = False

            newPerson = Person(name=staff_person['Name'], constrains=newConstrains, lastWeek=[], weekend=newWeekend)
            people.append(newPerson)
    return people

#
#
# lastWeek = ['repo', 'evening', 'evening', 'evening', 'morning', 'repo', 'evening']
# constrains = {'everyday': 'evening', 'Monday': 'morning'}
# myPerson = Person(name="test", constrains=constrains, lastWeek=lastWeek, repoThisMonth=False)

