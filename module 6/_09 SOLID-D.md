# Принцип инверсии зависимостей

Принцип инверсии зависимостей гласит:

* Модуль высокого уровня не должен зависеть от модулей низкого уровня. 
* И то, и другое должно зависеть от абстракций. 

* Абстракции не должны зависеть от деталей реализации. 

* Детали реализации должны зависеть от абстракций.

Если ваш код уже реализует `принципы открытости/закрытости` и подстановки Лисков, он уже будет неявно согласован с принципом инверсии зависимостей.  

Следуя принципу открытости/закрытости, вы создаете интерфейсы, которые можно использовать для предоставления различных высокоуровневых реализаций. 

Следуя принципу `подстановки Лисков`, вы гарантируете, что сможете заменить экземпляры класса низкого уровня объектами класса высокого уровня без какого-либо негативного воздействия на приложение. 

Таким образом, следуя этим двум принципам, вы гарантируете, что ваши классы высокого уровня и классы низкого уровня зависят от интерфейсов. 

Следовательно, вы неявно следуете принципу инверсии зависимостей.

Как показано в коде ниже, у нас есть класс `Student`, который мы используем для создания экземпляров `Student` и класса `Team`, который содержатся сведения о принадлежности учеников к разным командам.

Теперь мы определим высокоуровневый класс `Analysis`, где нам нужно отсеять всех учеников, принадлежащих красной команде.


```python
from enum import Enum


class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3


class Student:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self):
        self.team_member = []

    def add_team_member(self, student, team):
        self.team_member.append((student, team))


class Analysis:
    def __init__(self, team_student_member):
        member = team_student_member.team_member
        for members in member:
            if members[1] == Teams.RED_TEAM:
                print(f'{members[0].name} is in RED team')


student1 = Student('Олег')
student2 = Student('Сергей')
student3 = Student('Владимир')

team_member = Team()
team_member.add_team_member(student1, Teams.BLUE_TEAM)
team_member.add_team_member(student2, Teams.RED_TEAM)
team_member.add_team_member(student3, Teams.GREEN_TEAM)

Analysis(team_member)

```

Как видно из реализации, мы напрямую используем `team_student_member.team_member` в высокоуровневом классе `Analysis`, и мы используем реализацию этого списка непосредственно в классе высокого уровня. 

На данный момент все нормально, но представьте ситуацию, в которой нам нужно изменить эту реализацию со списка на что-то другое. 

В этом случае наш класс высокого уровня `Analysis` сломается, поскольку он зависит от деталей реализации `TeamMemberships` низкого уровня.

Теперь взгляните на пример ниже, в котором мы меняем эту реализацию и приводим ее в соответствие с принципом инверсии зависимостей.


```python
from enum import Enum
from abc import abstractmethod


class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3


class MemberTeamFind:
    @abstractmethod
    def find_all_students_of_team(self, team):
        pass


class Student:
    def __init__(self, name):
        self.name = name


class TeamMemberships(MemberTeamFind):
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students_of_team(self, team):
        for members in self.team_memberships:
            if members[1] == team:
                yield members[0].name


class Analysis:
    def __init__(self, team_team_member_find):
        for student in team_team_member_find.find_all_students_of_team(Teams.RED_TEAM):
            print(f'{student} is in RED team.')


student1 = Student('Олег')
student2 = Student('Сергей')
student3 = Student('Владимир')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)


```


Чтобы следовать принципу инверсии зависимостей, нам необходимо убедиться, что класс высокого уровня `Analysis` не зависит от конкретной реализации класса низкого уровня `TeamMembership`. 

Вместо этого он должен зависеть от некоторой абстракции.

Итак, мы создаем интерфейс `TeamMemberships`, который содержит абстрактный метод `find_all_students_of_team`, передающийся любому классу, наследующему этот интерфейс. 

Мы наследуем наш класс `TeamMembership` от этого интерфейса, следовательно, теперь класс `TeamMembership` должен предоставлять реализацию функции `find_all_students_of_team`.

Затем эта функция передает результаты любому другому вызывающему ее объекту.

Мы перенесли обработку, которая делалась в классе высокого уровня `Analysis` в `TeamMemberships` через интерфейс `TeamMemberships`.

Сделав все это, мы убрали зависимость класса `Analysis` от класса `TeamMemberships` и перенесли ее в интерфейс `TeamMemberships`. 

Теперь класс высокого уровня не зависит от деталей реализации класса низкого уровня. 

Любые изменения в деталях реализации класса низкого уровня не влияют на класс высокого уровня.