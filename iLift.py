from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy_declarative import Workout, Base
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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
	"""x1_list = []
	x2_list = []
	y1_list = []
	y2_list = []"""
	
	
	x1_list = [datetime.date(2016, 10, 30), datetime.date(2016, 10, 31), datetime.date(2016, 11, 2), datetime.date(2016, 11, 6), datetime.date(2016, 11, 10), datetime.date(2016, 11, 12)]
	x2_list = [datetime.date(2016, 11, 1), datetime.date(2016, 11, 3), datetime.date(2016, 11, 4), datetime.date(2016, 11, 5), datetime.date(2016, 11, 8), datetime.date(2016, 11, 9)]
	y1_list = [4000, 4230, 4300, 4050, 4203, 4030]
	y2_list = [6020, 6340, 6200, 6400, 6500, 6040]
	

	

	"""for workout in all_workouts:
		if workout.type == "log_lift":
			x1_list.append(workout.date)
			y1_list.append(workout.volume)
		elif workout.type == "bench_press":
			x2_list.append(workout.date)
			y2_list.append(workout.volume)
	"""
	
	fig = plt.figure() 
	fig.canvas.set_window_title('iLift') 
	plt.plot(x1_list,y1_list, label = "log lift")
	plt.plot(x2_list, y2_list, label = "bench press")
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.title('Volume')
	plt.legend()
	plt.show()
	plt.gcf().autofmt_xdate()
	print("Chart displayed!")
	

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

	
