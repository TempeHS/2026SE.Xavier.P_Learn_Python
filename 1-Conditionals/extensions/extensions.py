filetype = input("File name: ").split(".")[1]
filetype = filetype.strip().lower()

match filetype:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("image/png")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")