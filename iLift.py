from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy_declarative import Workout, Base
import datetime


def start_session():
	engine = create_engine('sqlite:///database.db')	 
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind = engine)
	session = DBSession()
	return session
	

def save_workout():
	print("type in the type of workout, the volume and the max kg; then press ENTER")
	expression = input()
	expression_list = expression.split()
	session = start_session()
	new_workout = Workout(type=expression_list[0], volume = int(expression_list[1]),
	                      max_kg = int(expression_list[2]), date = datetime.date.today())
	session.add(new_workout)
	session.commit()
	print("Workout succesfully saved!")


def show_workouts():
	session = start_session()
	all_workouts = session.query(Workout).all()
	for workout in all_workouts:
		print("id = " + str(workout.id) + ", type = " + workout.type + ", volume = " + str(workout.volume) +
		      ", max_kg = " + str(workout.max_kg) + ", date = " + str(workout.date))
	print("All workouts displayed!")
	

def delete_workout():
	session = start_session()
	print("Type in the ID of the workout you want to delete")
	input_id = input()
	workout = session.query(Workout).filter(Workout.id == input_id).first()
	session.delete(workout)
	session.commit()
	print("Workout " + input_id + " successfully deleted!")

	

	
running = True
print("BIG_volume SOFTWARE")
print("1) show my workouts")
print("2) save workout")
print("3) delete workout")
print("4) exit program")
while(running):
	print("Type an option..")
	choice = input()
	if choice == "1":
		show_workouts()
	elif choice == "2":
		save_workout()
	elif choice == "3":
		delete_workout()
	elif choice == "4":
		running = False
	elif choice == "load":
		pass
		"""
		session = start_session()
		volume1 = 4232
		volume2 = 6696
		volume3 = 4268
		max1 = 48
		max2 = 84
		max3 = 46
		date1 = datetime.date(2016, 10, 30)
		date2 = datetime.date(2016, 11, 1)
		date3 = datetime.date(2016, 11, 3)
		
		workout1 = Workout(type = "log_lift", volume = volume1, max_kg = max1, date = date1 )
		workout2 = Workout(type = "bench_press", volume = volume2, max_kg = max2, date = date2)
		workout3 = Workout(type = "log_lift", volume = volume3, max_kg = max3, date = date3)
		
		session.add(workout1)
		session.add(workout2)
		session.add(workout3)
		
		session.commit()
		
		print("Data loaded!")  """
		
	else:
		print("Wrong number!")

	
