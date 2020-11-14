local height = 2
local count = 0
local run = 0

function digProperly()
    while turtle.detect() do
        turtle.dig()
        os.sleep(0.5)
    end
end
function dig()
    if count%2 == 1
    then
        turtle.turnRight()
        for i = 1, 2 do
            turtle.digUp()
            turtle.digDown()
            digProperly()
            turtle.forward()
        end
        if count%10 == 1
        then
            turtle.back()
            turtle.turnRight()
            turtle.turnRight()
            turtle.select(3)
            turtle.place()
            turtle.turnLeft()
            turtle.turnLeft()
            turtle.forward()
        end
        turtle.digUp()
        turtle.digDown()
        turtle.turnLeft()
        digProperly()
        turtle.forward()
    else
        turtle.turnLeft()
        for i = 1, 2 do
            turtle.digUp()
            turtle.digDown()
            digProperly()
            turtle.forward()
        end
        turtle.digUp()
        turtle.digDown()
        turtle.turnRight()
        digProperly()
        turtle.forward()
    end
end
term.write("length of tunnel: ")
run = read()
local x = 0
for i = 1, run do
    count = count+1
    if turtle.getFuelLevel() < 2 then
        turtle.select(1)
        turtle.refuel(1)
    end
    if count%4 == 0
    then
        for i = 1, 16 do
            turtle.select(i)
            local details = turtle.getItemDetail()
            if details ~= nil then
                if details.name == "minecraft:cobblestone" or details.name == "minecraft:gravel" or details.name == "minecraft:dirt"
                then
                    turtle.drop()
                end
            end
        end
    end
    if turtle.getItemCount(2) > 32 then
        turtle.select(2)
        x = turtle.getItemCount(2)-1
        turtle.drop(x)
    end
    dig()
end