from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Workout(Base):
    __tablename__ = 'workout'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    volume = Column(Integer, nullable = False)
    max_kg = Column(Integer)
    date = Column(Date, nullable = False)
 

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
	
	
def create_span_dates(all_workouts):
	all_dates = []
	for workout in all_workouts:
		if workout.date not in all_dates:
			all_dates.append(workout.date)
	oldest_date = min(all_dates)
	youngest_date = max(all_dates)
	span_dates_list = []
	date = oldest_date
	while date < max(all_dates):
		span_dates_list.append(date)
		date += datetime.timedelta(days=5)
	return span_dates_list


def show_workouts():
	session = start_session()
	#all_workouts = session.query(Workout).all()
			
	all_workouts = [Workout(id = 1, type = "log_lift", volume = 4000, max_kg = 45, date = datetime.date(2016, 10, 30)),
					Workout(id = 2, type = "log_lift", volume = 4230, max_kg = 48, date = datetime.date(2016, 10, 31)),
					Workout(id = 3, type = "log_lift", volume = 4300, max_kg = 50, date = datetime.date(2016, 11, 2)),
					Workout(id = 4, type = "log_lift", volume = 4050, max_kg = 46, date = datetime.date(2016, 11, 6)),
					Workout(id = 5, type = "log_lift", volume = 4203, max_kg = 47, date = datetime.date(2016, 11, 10)),
					Workout(id = 6, type = "log_lift", volume = 4030, max_kg = 49, date = datetime.date(2016, 11, 12)),
					Workout(id = 7, type = "bench_press", volume = 6020, max_kg = 80, date = datetime.date(2016, 11, 1)),
					Workout(id = 8, type = "bench_press", volume = 6340, max_kg = 82, date = datetime.date(2016, 11, 3)),
					Workout(id = 9, type = "bench_press", volume = 6200, max_kg = 80, date = datetime.date(2016, 11, 4)),
					Workout(id = 10, type = "bench_press", volume = 6400, max_kg = 84, date = datetime.date(2016, 11, 5)),
					Workout(id = 11, type = "bench_press", volume = 6500, max_kg = 86, date = datetime.date(2016, 11, 8)),
					Workout(id = 12, type = "bench_press", volume = 6040, max_kg = 85, date = datetime.date(2016, 11, 9)),
				    Workout(id = 13, type = "squat", volume = 3000, max_kg = 40, date = datetime.date(2016, 11, 13)),
					Workout(id = 14, type = "squat", volume = 3200, max_kg = 45, date = datetime.date(2016, 11, 16)),
					Workout(id = 15, type = "squat", volume = 3350, max_kg = 36, date = datetime.date(2016, 11, 20))]
					
	workout_types = []

	for workout in all_workouts:
		if workout.type not in workout_types:
			workout_types.append(workout.type)
	print(workout_types)
	
	for workout in all_workouts:
		print("id = " + str(workout.id) + ", type = " + workout.type + ", volume = " + str(workout.volume) +
				  ", max_kg = " + str(workout.max_kg) + ", date = " + str(workout.date))
	print("All workouts displayed!")
		
	plt.subplot(2, 1, 1)
	all_x_lists = []		
	for type in workout_types:
		x_list = []
		y_list = []
		for workout in all_workouts:
			if workout.type == type:
				x_list.append(workout.date)
				y_list.append(workout.volume)	
		plt.plot(x_list,y_list, label = type)
		plt.ylabel('Volume')
		plt.legend(prop={'size':10})
		all_x_lists += x_list
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.xticks(create_span_dates(all_workouts))

	plt.subplot(2, 1, 2)
	all_x_lists = []
	for type in workout_types:
		x_list = []
		y_list = []
		for workout in all_workouts:
			if workout.type == type:
				x_list.append(workout.date)
				y_list.append(workout.max_kg)	
		plt.plot(x_list,y_list, label = type)
		plt.ylabel('Max kg')
		plt.xlabel('month/day')
		plt.legend(prop={'size':10})
		all_x_lists += x_list
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.xticks(create_span_dates(all_workouts))
	
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

	
def main():
	db_file = Path("/database.db")
	if not db_file.is_file():
		engine = create_engine('sqlite:///database.db')
		Base.metadata.create_all(engine)	
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
		else:
			print("Wrong number!")


if __name__ == "__main__":
    main()

	
