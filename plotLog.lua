-- plot which column ? pass the #column as cmdline args
-- Jie Lei

require 'gnuplot'


-- Read data from file

function read_file_str(path)
    local f = assert(io.open(path, "r"))
    local c = f:read "*a"
    f:close()
    return c
end
logFile = read_file_str(arg[1])
logTable = string.split(logFile, '\n')

print('This file contrains entries '..logTable[1])
print('\n')

column = {}
for i = 2, #logTable do
   tmp = string.split(logTable[i], '\t')
   table.insert(column, tmp[tonumber(arg[2])])
end
column = torch.Tensor(column)


-- Start plotting
gnuplot.figure(1)
gnuplot.plot(column, '-')
gnuplot.xlabel('#epoch')
gnuplot.ylabel(string.split(logTable[1], '\t')[tonumber(arg[2])])

-- save or not
--gnuplot.pngfigure('trainLoss.png')
--gnuplot.title('training loss over epoch')
--gnuplot.plot(avgLoss, '-')
--gnuplot.xlabel('#epoch')
--gnuplot.ylabel('Loss')
--gnuplot.plotflush()


