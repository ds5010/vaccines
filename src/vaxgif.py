#Kayne Ryan
#DS5010 Spring 2022

#gif for vax project

import graphicsPlus as gp
import time

def over_time(img1, img2, img3, img4, img5, img6, img7):
  area = 300
  one = gp.Image(gp.Point(area, area), img1)
  two = gp.Image(gp.Point(area, area), img2)
  three = gp.Image(gp.Point(area, area), img3)
  four = gp.Image(gp.Point(area, area), img4)
  five = gp.Image(gp.Point(area, area), img5)
  six = gp.Image(gp.Point(area, area), img6)
  seven = gp.Image(gp.Point(area, area), img7)

  cols = one.getWidth()
  rows = one.getHeight()
  win = gp.GraphWin("Vaccination rate vs. Death Rate, June 1-Nov 30 2021", cols, rows)

  for i in range (700):
    if i == 0:
      one.draw(win)
      win.update()
    elif i == 50:
      two.draw(win)
      one.undraw()
      win.update()
    elif i == 100:
      three.draw(win)
      two.undraw()
      win.update()
    elif i == 150: 
      four.draw(win)
      three.undraw()
      win.update()
    elif i == 200:
      five.draw(win)
      four.undraw()
      win.update()
    elif i == 250: 
      six.draw(win)
      five.undraw()
      win.update()
    elif i == 300:
      seven.draw(win)
      six.undraw()
      win.update()
    elif i == 350:
      one.draw(win)
      seven.undraw()
      win.update()
    elif i == 400:
      two.draw(win)
      win.update()
    elif i == 450:
      three.draw(win)
      win.update()
    elif i == 500: 
      four.draw(win)
      win.update()
    elif i == 550:
      five.draw(win)
      win.update()
    elif i == 600: 
      six.draw(win)
      win.update()
    elif i == 650:
      seven.draw(win)
      win.update()
    elif i == 700:
      win.close()
    time.sleep(0.02)

if __name__ == "__main__":
    over_time('images/june.ppm', 'images/july.ppm', 'images/aug.ppm', 'images/sep.ppm', 'images/oct.ppm', 'images/nov.ppm', 'images/nov30.ppm')