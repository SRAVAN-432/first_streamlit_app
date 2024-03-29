import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('my parents new health dinner');
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-range egg ')
streamlit.text('🥑🍞avocad toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#streamlit.header('Fruityvice Fruit Advice!')
##try:
    #fruit_choice = streamlit.text_input('What fruit would you like information about?')
    #if not fruit_choice:
        #streamlit.error("please select a fruit to get information.")
    #else:
        #back_from_function=get_fruityvice_data(fruit_choice)
        #streamlit.dataframe(back_from_function)
#except URLError as e:
    #streamlit.error()



#import snowflake.connector
#streamlit.header("the fruit load list contains:")

#def get_fruit_load_list():
   # with my_cnx.cursor() as my_cur:
         #my_cur.execute("SELECT * FROM fruit_load_list")
         #return my_cur.fetchall()
#if streamlit.button('get fruit load list'):
    #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]
        #my_data_rows = get_fruit_load_list()
    #streamlit.dataframe(my_rows)


#streamlit.stop()
#def insert_row_snowflake(new_fruit);
   #with my_cnx.cursor() as my_cur:                                   
   #my_cur.execute(" Insert into fruit_load_list values (' + ???? +')")
   #return "thanks for adding" + new_fruit
#add_my_fruit= streamlit.text_input('What fruit would you like to add?')
#if streamlit.button('add a fruit to the list'):
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]
#back_from_funtion=insert_row_snowflake(add_my_fruit)
#streamlit.text(back_from_function)
                                     
#streamlit.write('Thanks for adding ', add_my_fruit)

#my_cur.execute(" Insert into fruit_load_list values ('from streamlit')")
