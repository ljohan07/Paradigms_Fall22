trackRobot = (north, east, south, west) -> 
    location = [0, 0]
    if north?
        location[1] += north
    if east?
        location[0] += east
    if south?
        location[1] -= south
    if west?
        location[0] -= west
    return location


module.exports = { trackRobot }