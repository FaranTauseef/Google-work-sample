"""A video player class."""

from .video_library import VideoLibrary
import random
import re
video_playing = "no"
video_state = "e"

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        #"""Returns all videos."""
        print("List of Videos")
        videos= self._video_library.get_all_videos()
        temp_list=[]
        for vid in videos:
            tag_list = " "
            for curr_tag in vid.tags:
                tag_list = tag_list + curr_tag + " "

            temp_list += [f"{vid.title} ({vid.video_id}) [{tag_list}]"]
        sorted_list=sorted(temp_list)
        for x in sorted_list:
            print(x)

        #print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global video_playing
        global video_state
        
        if video_playing == "no":
           video_playing = video_id
           video_state= "play"
           print("playing: " + video_playing)
        else:
            self.stop_video()
            video_playing = video_id
            video_state="play"
            print("playing: " + video_playing)

        #print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        global video_playing
        global video_state
        if video_playing == "no":
            print("cannot stop video: video does not exist")
        else:
            print("stoping: " + video_playing)
            video_playing = "no"
            video_state="e"
        
        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        num_videos = len(self._video_library.get_all_videos())
        num = random.randint(0,num_videos-1)
        videos= self._video_library.get_all_videos()
        temp_list=[]
        for vid in videos:
            tag_list = " "
            for curr_tag in vid.tags:
                tag_list = tag_list + curr_tag + " "

            temp_list += [f"{vid.title} ({vid.video_id}) [{tag_list}]"]
        sorted_list=sorted(temp_list)

        self.play_video(sorted_list[num])

        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        global video_playing
        global video_state
        if video_state == "e":
            print("cannot pause video: no video is currently playing")
        else:
            if video_state=="p":
                print("video already paused" + video_playing)
            else:
                video_state="p"
                print("pausing video: " + video_playing)

        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        global video_playing
        global video_state

        if video_state == "p":
            video_state="play"
            print("continuing video: " + video_playing)
        else:
            if video_state == "e":
                print("cannot continue video: no video is currently playing")
            else: 
                if video_state == "play":
                    print("cannot continue video: video is not paused") 
       
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        global video_state
        global video_playing
        
        temp_var=[]
        videos= self._video_library.get_all_videos()
        if video_state=="play":
            
            for vid in videos:
                
                if vid.video_id == video_playing:
                    
                    temp_var = f"{vid.title} ({vid.video_id}) {vid.tags}"
                    print (temp_var)
        else:
            if video_state=="p":
                 for vid in videos:
                    if vid.video_id == video_playing:
                        temp_var= f"{vid.title} ({vid.video_id}) {vid.tags}"
                        print(temp_var + " - paused") 
            else:
                if video_state=="e":
                    print("no video is playing")



        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos= self._video_library.get_all_videos()
        temp_list=[]
        for vid in videos:
            #print(search_term.lower())
            #print(vid)
            #print(vid.title.lower().find(search_term.lower()))
            if vid.title.lower().find(search_term.lower()) != -1:
                
            #if search_term.lower()==curr_name.lower():


                temp_list += [f"{vid.title} ({vid.video_id}) [{vid.tags}]"]
        sorted_list=sorted(temp_list)
        count=1
        for x in sorted_list:
            print(str(count) + ") " + x)
            count=count + 1

        """print("Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no.")
        val = input("Enter your value: ")
        print(len(sorted_list))
        if int(val) > 0 and int(val) <= int(len(sorted_list)):
            self.play_video(sorted_list[val-1].video_id)

        """
        #print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos= self._video_library.get_all_videos()
        temp_list=[]
        for vid in videos:
            #print(search_term.lower())
            #print(vid)
            #print(vid.title.lower().find(search_term.lower()))
            #print(vid.tags)
            for curr_tag in vid.tags:
                if curr_tag.lower()==video_tag.lower():
                
            #if search_term.lower()==curr_name.lower():


                    temp_list += [f"{vid.title} ({vid.video_id}) [{vid.tags}]"]
        sorted_list=sorted(temp_list)

        count=1
        for x in sorted_list:
            print(str(count) + ") " + x)
            count+=1

        #print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
