from math import sqrt 

def distance(point1, point2):

  x_diff = point1[0] - point2[0]
  y_diff = point1[1] - point2[1]
  return sqrt(x_diff**2 + y_diff**2)

def find_closest_pairs(plane_data):
 
  if len(plane_data) < 2:
    raise ValueError("K porovnání jsou potřeba alespoň dvě letadla")

  min_dist = float('inf')
  closest = []
  for i in range(len(plane_data)):
    for j in range(i + 1, len(plane_data)):
      current_dist = distance(plane_data[i][0], plane_data[j][0])
      if current_dist < min_dist:
        min_dist = current_dist
        closest = [(plane_data[i][1], plane_data[j][1])]
      elif current_dist == min_dist:
        closest.append((plane_data[i][1], plane_data[j][1]))
  return min_dist, closest

def parse_plane_data():
 
  planes = []
  while True:
    line = input()
    if not line:
      break
    try:
      coords, name = line.split(':')
      x, y = map(float, coords.split(','))
      planes.append(((x, y), name))
    except Exception:
      print("Chyba: nesprávně zadaný formát")
      break
  return planes

def main():
  
  planes = parse_plane_data()
  if len(planes) < 2:
    print("Chyba: méně než dvě letadla na vstupu")
  else:
    min_distance, closest_pairs = find_closest_pairs(planes)
    print("Vzdálenost nejbližších letadel: {:.6f}".format(min_distance))
    print("Počet nalezených dvojic: {}".format(len(closest_pairs)))
    for pair in closest_pairs:
      print(" - ".join(pair))

if __name__ == "__main__":
  main()
