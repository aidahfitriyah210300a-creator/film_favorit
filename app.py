  from flask import Flask, render_template, request, redirect, url_for, flash

  app = Flask(__name__)

  app.secret_key = "ganti_dengan_rahasia"

  movies = []
  next_id = 1

  @app.route("/")
  def index():
      return render_template("index.html", movies=movies)

  @app.route("/add", methods=["GET", "POST"])
  def add():
      global next_id
      if request.method == "POST":
          title = request.form.get("title", "").strip()
          director = request.form.get("director", "").strip()
          rating = request.form.get("rating", "0").strip()
          if not title:
              flash("Judul wajib diisi", "danger")
              return redirect(url_for("add"))
          try:
              rating = float(rating)
          except:
              rating = 0.0
          movie = {"id": next_id, "title": title, "director": director, "rating": rating}
          movies.append(movie)
          next_id += 1
          flash("Film ditambahkan", "success")
          return redirect(url_for("index"))
      return render_template("add.html")

  if __name__ == "__main__":
      app.run(debug=True)
  
