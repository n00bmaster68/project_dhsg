from camera import get_image_by_webcam
from crawl_titles import get_titles_on_web
from natural_language_processing import get_name_of_object_in_image

if __name__ == "__main__":
	filePath = get_image_by_webcam()
	titles = get_titles_on_web(filePath)
	get_name_of_object_in_image(titles)