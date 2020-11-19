local y = 70
local x = 1
local z = 1

function refuel()
    if turtle.detect() 
    then
        turtle.dig()
    end
    turtle.select(1)
    turtle.place()
    turtle.suck()
    turtle.refuel()
    turtle.drop()
    turtle.dig()
end

function dig_properly()
    while turtle.detect() do
        turtle.dig()
        os.sleep(0.5)
    end
end

refuel()
while y ~= 4 do
    for i = 1, 3 do
        turtle.digDown()
        turtle.down()
    end
    while z < 17 do
        while x < 16 do
            if x == 8
            then
                if z % 4 == 0
                then
                while turtle.detect() do
                    turtle.dig()
                    os.sleep(0.5)
                end
                turtle.select(1)
                turtle.place()
                for i = 2, 16 do
                    turtle.select(i)
                    turtle.drop()
                end
                turtle.select(1)
                turtle.drop()
                turtle.dig()
                if turtle.getFuelLevel() < 100 
                then
                    refuel()
                end
                end
            end
            turtle.digUp()
            turtle.digDown()
            dig_properly()
            turtle.forward()
            x = x + 1
        end
        turtle.digUp()
        turtle.digDown()
        x = 1
        if z < 16
        then
            if z % 2 == 1 
            then
                turtle.turnRight()
                dig_properly()
                turtle.forward()
                turtle.turnRight()
            else
                turtle.turnLeft()
                dig_properly()
                turtle.forward()
                turtle.turnLeft()
            end
        else
            turtle.turnRight()
            for i = 1, 16 do
                turtle.forward()
            end
            turtle.turnRight()
        end
        z = z + 1
    end
    z = 1
end

    