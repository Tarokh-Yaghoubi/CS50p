# Detect file extensions in Python Programming , CS50P

def main():
    file_name = input("Enter a file name : ").lower().strip()
    check_ext(file_name)
    
def check_ext(filename):
    ext = filename.split(".")
    ext = ext[-1]
    match ext:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "gif":
            print("image/gif")
        
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
            

main()