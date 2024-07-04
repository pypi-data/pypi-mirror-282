import os, customtkinter
import csv
import geopy.distance
from tkintermapview import TkinterMapView
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from multi_vids_merge import merge_videos
from gopro_main import multi_vids_extraction
from tkcalendar import DateEntry
from PIL import Image, ImageTk

customtkinter.set_default_color_theme("blue")

customtkinter.set_appearance_mode("System")


class App(customtkinter.CTk):

    APP_NAME = "Geospatial Image on Map Viewer"
    WIDTH = 800
    HEIGHT = 500

    # Default location is Blacksburg, VA
    VT_LAT = 37.2249991 
    VT_LON = -80.4249983

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        self.image_frame_directory = ""
        self.lat_lon_csv_file = ""
        self.frame_frequency_value = 10

        self.img_proximity_value = 5.00

        # ============ create CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(2, weight=1)

        # ============ Frame rate ============
        # Create a label for the frame frequency entry field
        self.frame_frequency_label = customtkinter.CTkLabel(self.frame_left, text="Seconds per Frame:", anchor="w")
        self.frame_frequency_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))
        
        # Create an entry field for the user to enter the frame frequency
        self.frame_frequency_entry = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Enter sec per frame")
        self.frame_frequency_entry.grid(row=1, column=0, padx=(20, 20), pady=(10, 0))        

        # Bind the "Return" key to the frame_frequency method
        self.frame_frequency_entry.bind(sequence="<Return>", command=self.frame_frequency)

        # ============ Select Output Folder ============
        self.output_folder_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Select Output Folder",
                                                command=self.get_image_output_folder)
        self.output_folder_button.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        # ============ Open Video File(s) ============
        self.video_file_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Open Video File(s)",
                                                command=self.open_file_command)
        self.video_file_button.grid(pady=(20, 0), padx=(20, 20), row=3, column=0)

        # ============ Merge Video File(s) ============
        self.merge_video_files_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Merge Video Files",
                                                command=self.merge_vids_command)
        self.merge_video_files_button.grid(pady=(20, 0), padx=(20, 20), row=4, column=0)

        # ============ Latitude Longitude Search Button ============
        self.lat_lon_search_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Select Lat-Lon CSV",
                                                command=self.select_lat_lon_csv_file)
        self.lat_lon_search_button.grid(pady=(20, 0), padx=(20, 20), row=5, column=0)

        # ============ Latitude Longitude Map Button ============
        self.select_frame_directory_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Select Frame Folder",
                                                command=self.select_frame_directory)
        self.select_frame_directory_button.grid(pady=(20, 0), padx=(20, 20), row=6, column=0)

        # ============ Latitude Longitude Image Generate Button ============
        self.create_lat_lon_image_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Create Lat-Lon Image",
                                                command=self.create_lat_lon_image)
        self.create_lat_lon_image_button.grid(pady=(20, 0), padx=(20, 20), row=7, column=0)

        # ============ Latitude Longitude Map Button ============
        self.lat_lon_search_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Map Lat-Lon",
                                                command=self.map_lat_lon)
        self.lat_lon_search_button.grid(pady=(20, 0), padx=(20, 20), row=8, column=0)

        # ============ Frame rate ============
        # Create a label for the frame frequency entry field
        self.img_proximity_label = customtkinter.CTkLabel(self.frame_left, text="Image Proximity (in meters)", anchor="w")
        self.img_proximity_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))
        
        # Create an entry field for the user to enter the frame frequency
        self.img_proximity_entry = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="(Default value is 5.00)")
        self.img_proximity_entry.grid(row=10, column=0, padx=(20, 20), pady=(10, 0))        

        # Bind the "Return" key to the frame_frequency method
        self.img_proximity_entry.bind(sequence="<Return>", command=self.img_proximity_func)
        
        # ============ Appearance Mode ============
        # self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=8, column=0, padx=(20, 20), pady=(20, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode)
        # self.appearance_mode_optionemenu.grid(row=9, column=0, padx=(20, 20), pady=(10, 20))

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))


        # ============ Latitude Longitude Search Bar ============
        # self.lat_long_entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                     placeholder_text="type as \"latitude, longitude\"")
        # self.lat_long_entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        # self.lat_long_entry.bind(sequence="<Return>", command=self.lat_lon_event)
        # self.lat = App.VT_LAT
        # self.lon = App.VT_LON

        # self.date_entry = DateEntry(self.frame_right, width=12, borderwidth=2, year=2023)
        # self.date_entry.grid(row=0,column=1,padx=20)

        # self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                         text="Search",
        #                                         width=30,
        #                                         command=self.search_lat_lon_date_event)
        # self.button_5.grid(row=0, column=2, sticky="w", padx=(12, 0), pady=12)

        # ============ progressbar ============
        # self.pb = ttk.Progressbar(
        #     self.frame_left,
        #     orient='horizontal',
        #     mode='indeterminate',
        #     length=140
        # )

        # # place the progressbar
        # self.pb.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

        # ============ Map Search ============
        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="Type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)


        # ============ Map (Tile Server) ============
        # self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
        # self.map_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))

        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_right, 
                                                           values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                           command=self.change_map)
        self.map_option_menu.grid(row=0, column=2, padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Virginia Tech")
        self.map_option_menu.set("OpenStreetMap")
        # self.appearance_mode_optionemenu.set("Dark")


    # def lat_lon_event(self, event):
    #     """
    #     @deprecated
    #     This function is called when the user presses the "Search" button beside the latitude or longitude entry field.
    #     It gets the values from the entry fields and passes them to the map widget.

    #     """
    #     self.lat = self.lat_long_entry.get().split(",")[0]
    #     self.lon = self.lat_long_entry.get().split(",")[1]

    #     print(f"Latitude: {self.lat}")
    #     print(f"Longitude: {self.lon}")
        # self.map_widget.set_lat_lon(self.lat, self.lon)

    # def search_lat_lon_date_event(self):
    #     """
    #     @deprecated
    #     This function is called when the user presses the "Search" button beside the date entry field.
    #     It gets the value from the entry field and passes it to the map widget.

    #     """
    #     self.date = self.date_entry.get_date()

    #     if self.lat_long_entry.get() != "":
    #         self.lat = self.lat_long_entry.get().split(",")[0]
    #         self.lon = self.lat_long_entry.get().split(",")[1]

    #     print(f"Latitude: {self.lat}")
    #     print(f"Longitude: {self.lon}")
    #     print(f"Date: {self.date}")

    def frame_frequency(self, event):
        """
        This function is called when the user presses the "Return" key in the frame frequency entry field.
        It gets the value from the entry field and prints it to the console.
        """
        self.frame_frequency_value = self.frame_frequency_entry.get()
        # print(f"Frame rate: {self.frame_frequency_value}")

    def img_proximity_func(self, event):
        """
        This function is called when the user presses the "Return" key in the image proximity entry field.
        It gets the value from the entry field and prints it to the console.
        """
        self.img_proximity_value = self.img_proximity_entry.get()
        # print(f"Image Proximity: {self.img_proximity_value}")

    def select_lat_lon_csv_file(self):
        """
        This function is called when the user clicks the "Select CSV File" button.
        It opens a file dialog and allows the user to select a csv file.
        The csv file should contain a list of latitude and longitude coordinates.
        """
        # Set filetypes
        filetypes = (
            ('CSV files', '*.csv'),
            ('All files', '*.*')
        )
        
        # Open file dialog
        self.lat_lon_csv_file = fd.askopenfilename(
            title='Open file',
            initialdir='/',
            filetypes=filetypes
        )

    def select_frame_directory(self):
        """
        This function is called when the user clicks the "Select frame folder" button.
        The directory is then saved to the self.image_frame_directory variable.
        """
        self.image_frame_directory = fd.askdirectory(title='Select frame folder')
    
    def create_lat_lon_image(self):
        """
        This function is called when the user clicks the "Create Lat-Lon Image" button.
        It uses the latitude and longitude values from the entry field to place a marker on the map.
        """
        # Check if all fields are filled
        if self.image_frame_directory == "":
            mb.showinfo(title="Create Lat-Lon Image",  message="[X] Image Output Directory not selected!", icon='error')
            return
        if self.lat_lon_csv_file == "":
            mb.showinfo(title="Create Lat-Lon Image",  message="[X] Lat-Lon File not selected!", icon='error')
            return

        # Read CSV file into a dictionary
        frame_list = []
        time = []
        lat = []
        lon = []
        with open(self.lat_lon_csv_file, 'r') as lat_lon_csv_file:
             csv_reader = csv.reader(lat_lon_csv_file)
             header = next(csv_reader)
             for row in csv_reader:
                time.append(row[0]) 
                lat.append(row[1])
                lon.append(row[2])
                frame_list.append(f"{row[0]}_{row[1]}_{row[2]}")

        # Read all the image names in the self.image_frame_directory directory
        image_list = []
        for filename in os.listdir(self.image_frame_directory):
            image_list.append(filename)
        
        # print(f"Image list: {image_list}")

        image_time = []
        image_lat = []
        image_lon = []
        for image in image_list:
            # print(f"Image: {image}")
            # print(f"Image split: {image.split('_')}")
            if len(image.split("_")) > 3:
                image_time.append(image.split("_")[1])
                image_lat.append(image.split("_")[2])
                image_lon.append(image.split("_")[3].split(".jpg")[0])
            else:
                continue

        closest_image_frame = {}
        # print(f"len(lat): {len(lat)}")
        # print(f"len(image_lat): {len(image_lat)}")

        # This code snippet iterates through the latitude and longitude coordinates 
        # of a given set of locations and compares them to a set of image latitude 
        # and longitude coordinates. It calculates the distance between each location 
        # and image using the geodesic distance formula from the geopy library. 
        # If the distance is less than or equal to 5 meters, it adds the corresponding 
        # image to a dictionary with the location coordinates as the key. 
        # Otherwise, it adds "N/A" to the dictionary.
        # The loop breaks once a matching image is found for each location.
        for i in range(len(lat)):
            for j in range(len(image_lat)):
                # print(f"Lat: {lat[i]}")
                # print(f"Lon: {lon[i]}")
                # print(f"Image Lat: {image_lat[j]}")
                # print(f"Image Lon: {image_lon[j]}")
                distance = geopy.distance.geodesic(
                    (float(lat[i]), float(lon[i])), 
                    (float(image_lat[j]), float(image_lon[j]))).meters
                # print(f"Distance: {distance}")
                if distance <= float(self.img_proximity_value):
                    closest_image_frame[(lat[i], lon[i])] = image_list[j]
                    break
                if (lat[i], lon[i]) not in closest_image_frame:
                    closest_image_frame[(lat[i], lon[i])] = "N/A"
        
        # print(f"Closest image frame: {closest_image_frame}")
        # print(f"Closest image frame length: {len(closest_image_frame)}")

        # Find the closest image to each lat-lon coordinate
        # for i in range(len(lat)):
        #     closest_image = ""
        #     for image in image_list:
        #         image_time = image.split("_")[0]
        #         image_lat = image.split("_")[1]
        #         image_lon = image.split("_")[2]
        #         if image_time == time[i] and image_lat == lat[i] and image_lon == lon[i]:
        #             closest_image = image
        #             break
        #     print(f"Closest image: {closest_image}")

        # coords_1 = (lat[0], lon[0])
        # coords_2 = (lat[1], lon[1])
        # distance = geopy.distance.geodesic(coords_1, coords_2).meters
        # print(f"Distance: {distance}")

        # Write all the rows to a csv file
        # This code snippet writes the time, latitude, longitude, and closest image frame to a CSV file. 
        # It opens a file in write mode and creates a csv writer object. It then iterates through the time, 
        # latitude, and longitude lists and writes each row to the CSV file. The closest image frame is 
        # determined by looking up the corresponding latitude and longitude coordinates in a dictionary. 
        # The loop breaks once all rows have been written to the CSV file.
        with open(f"{self.image_frame_directory}/lat-lon-frame.csv", 'w', newline='') as lat_lon_csv_file:
            csv_writer = csv.writer(lat_lon_csv_file)
            csv_writer.writerow(["Time", "Latitude", "Longitude", "Frame"])
            for i in range(len(time)):
                csv_writer.writerow([time[i], 
                                     lat[i], 
                                     lon[i], 
                                     closest_image_frame[(lat[i], lon[i])]
                                     ])
        
        mb.showinfo(title="Create Lat-Lon Image",  message="[√] Successfully created Lat-Lon-Frame CSV!", icon='info')

    
    def map_lat_lon(self):
        """
        This function is called when the user clicks the "Map Lat-Lon" button.
        It uses the latitude and longitude values from the entry field to place a marker on the map.
        """
        # Check if all fields are filled
        if self.image_frame_directory == "":
            mb.showinfo(title="Map Lat-Lon",  message="[X] Image Output Directory not selected!", icon='error')
            return
        if self.lat_lon_csv_file == "":
            mb.showinfo(title="Map Lat-Lon",  message="[X] Lat-Lon File not selected!", icon='error')
            return

        # Read CSV file into a dictionary
        frame_list = []
        time = []
        lat = []
        lon = []
        with open(self.lat_lon_csv_file, 'r') as lat_lon_csv_file:
             csv_reader = csv.reader(lat_lon_csv_file)
             header = next(csv_reader)
             for row in csv_reader:
                time.append(row[0]) 
                lat.append(row[1])
                lon.append(row[2])
                frame_list.append(f"{row[0]}_{row[1]}_{row[2]}")
        
        # Iterate through "time" list and put markers on the map
        for i in range(len(time)):
            image_path = os.path.join(self.image_frame_directory, f"frame_{frame_list[i]}.jpg")
            plane_image = ImageTk.PhotoImage(Image.open(image_path).resize((80, 80)))
            self.map_widget.set_marker(float(lat[i]), 
                                       float(lon[i]), 
                                       image=plane_image)

    def open_file_command(self):
        """
        This function is called when the user clicks the "Open Video File(s)" button.
        It opens a file dialog and allows the user to select video file(s).
        The video file(s) are then opened and images are extracted from it.
        The images are output to a selected or default new folder under the current working directory.
        """

        # Set filetypes
        filetypes = (
            ('Video files', '*.mp4'),
            ('All files', '*.*')
        )
        
        # Open file dialog
        self.filename = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes
        )

        if self.image_output_directory == None:
                self.image_output_directory = r'Output'
        if not os.path.exists(self.image_output_directory):
                os.makedirs(self.image_output_directory)

        # If file(s) are selected
        if self.filename:

            # self.pb['value'] = 100

            success_flag = multi_vids_extraction(vid_list=self.filename, 
                                                 output_dir=self.image_output_directory,
                                                 frames_after_number_of_seconds=int(self.frame_frequency_value))

            self.pop_up_message_on_succes(success_flag, "[√] Successfully extracted image and metadata!")

            # self.pb['value'] = 0

    
        # def open_file_command(self):
        # """
        # @deprecated
        # This function is called when the user clicks the "Open Video File(s)" button.
        # It opens a file dialog and allows the user to select a video file.
        # The video file is then opened and images are extracted from it.
        # The images are output to a selected or default new folder under the current working directory.
        # """

        # # Set filetypes
        # filetypes = (
        #     ('Video files', '*.mp4'),
        #     ('All files', '*.*')
        # )
        
        # # Open file dialog
        # self.filename = fd.askopenfilenames(
        #     title='Open files',
        #     initialdir='/',
        #     filetypes=filetypes
        # )

        # # If file(s) are selected
        # if self.filename:
        #     # Open video player
        #     self.video_capture = cv2.VideoCapture(self.filename[0])
        #     success,image = self.video_capture.read()
        #     print("success: " + str(success))

        #     success_flag = success

        #     count = 0

        #     if self.image_output_directory == None:
        #         self.image_output_directory = r'Images_CV'
        #     if not os.path.exists(self.image_output_directory):
        #         os.makedirs(self.image_output_directory)

        #     while success:
        #         # save frame as JPEG file      
        #         cv2.imwrite(os.path.join(self.image_output_directory , "frame%d.jpg" % count), image)     
        #         success,image = self.video_capture.read()
        #         print('Read a new frame: ', success)
        #         count += 1

        #     self.pop_up_message_on_succes(success_flag, "[√] Success!")

    
    def merge_vids_command(self):
        """
        This function is called when the user clicks the "Merge Video Files" button.
        It opens a file dialog and allows the user to select multiple MP4 video files.
        The video files are then merged into a single video file.
        """

        # Set filetypes
        filetypes = (
            ('Video files', '*.MP4'),
            ('All files', '*.*')
        )
        
        # Open file dialog
        self.filename = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes
        )

        if self.image_output_directory == None:
                self.image_output_directory = r'Output'
        if not os.path.exists(self.image_output_directory):
                os.makedirs(self.image_output_directory)

        output_filename = os.path.join(self.image_output_directory, "merged_vids.MP4")

        # If file(s) are selected
        if self.filename:
            # Merge video files
            success_flag = merge_videos(self.filename, output_filename)

            self.pop_up_message_on_succes(success_flag, "[√] Successfully merged videos!")

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def get_image_output_folder(self):
        """
        This function is called when the user clicks the "Select Image Output Folder" button.
        The directory is then saved to the self.image_output_directory variable.
        """
        self.image_output_directory = fd.askdirectory(title='Select image output folder')
        print(self.image_output_directory) 

    # deprecated
    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    # deprecated
    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    # deprecated
    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()
    
    def pop_up_message_on_succes(self, success_flag, message_str=""):
        """
        This function is called when the after the video to image frame conversion is complete.

        Args:
            success_flag (string): This flag is used to determine if video file(s) were successfully opened.
            message_str (str, optional): This is the string that gets printed when 
                the video to image frame conversion is successfully completed
                Defaults to "".
        """
        if success_flag:
            mb.showinfo(title="Video to Image Frame",  message=message_str, icon='info')
        else:
            mb.showinfo(title="Video to Image Frame",  message="[X] Failed!", icon='error')


if __name__ == "__main__":
    app = App()
    app.start()