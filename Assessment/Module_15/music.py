import os
import tkinter as tk
from tkinter import messagebox

# ---------- Playlist Class ----------
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def save_to_file(self):
        if not os.path.exists("playlists"):
            os.mkdir("playlists")

        filename = f"playlists/playlist_{self.name}.txt"

        if os.path.exists(filename):
            raise FileExistsError("Playlist already exists")

        with open(filename, "w", encoding="utf-8") as file:
            for song in self.songs:
                file.write(song + "\n")


# ---------- Main Application ----------
class MusicBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MusicBox")
        self.root.geometry("600x400")

        # Playlist Name
        tk.Label(root, text="Playlist Name").pack()
        self.playlist_entry = tk.Entry(root, width=40)
        self.playlist_entry.pack(pady=5)

        # Songs Text Area
        tk.Label(root, text="Song Titles (one per line)").pack()
        self.songs_text = tk.Text(root, height=8, width=50)
        self.songs_text.pack(pady=5)

        # Save Button
        tk.Button(root, text="Save Playlist", command=self.save_playlist).pack(pady=5)

        # Playlist Listbox
        tk.Label(root, text="Saved Playlists").pack()
        self.playlist_listbox = tk.Listbox(root, width=40)
        self.playlist_listbox.pack(pady=5)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.load_playlist)

        self.load_playlists()

    # ---------- Save Playlist ----------
    def save_playlist(self):
        name = self.playlist_entry.get().strip()
        songs = self.songs_text.get("1.0", tk.END).strip().split("\n")

        if not name:
            messagebox.showerror("Error", "Playlist name cannot be empty")
            return

        if not songs or songs == [""]:
            messagebox.showerror("Error", "Song list cannot be empty")
            return

        try:
            playlist = Playlist(name, songs)
            playlist.save_to_file()
            messagebox.showinfo("Success", "Playlist saved successfully")
            self.clear_inputs()
            self.load_playlists()
        except FileExistsError:
            messagebox.showerror("Error", "Playlist with this name already exists")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------- Load Playlist Names ----------
    def load_playlists(self):
        self.playlist_listbox.delete(0, tk.END)

        if not os.path.exists("playlists"):
            return

        for file in os.listdir("playlists"):
            if file.startswith("playlist_") and file.endswith(".txt"):
                name = file.replace("playlist_", "").replace(".txt", "")
                self.playlist_listbox.insert(tk.END, name)

    # ---------- Load Selected Playlist ----------
    def load_playlist(self, event):
        try:
            selection = self.playlist_listbox.curselection()
            if not selection:
                return

            name = self.playlist_listbox.get(selection[0])
            filename = f"playlists/playlist_{name}.txt"

            with open(filename, "r", encoding="utf-8") as file:
                songs = file.read()

            self.playlist_entry.delete(0, tk.END)
            self.playlist_entry.insert(0, name)

            self.songs_text.delete("1.0", tk.END)
            self.songs_text.insert(tk.END, songs)

        except FileNotFoundError:
            messagebox.showerror("Error", "Playlist file not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        self.playlist_entry.delete(0, tk.END)
        self.songs_text.delete("1.0", tk.END)


# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicBoxApp(root)
    root.mainloop()
