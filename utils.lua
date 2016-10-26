-- File I/O
function readJson(file)
    local cjson = require 'cjson';
    local f = io.open(file, "rb")
    local content = f:read("*all")
    f:close()
    return cjson.decode(content)
end


--save simple lua table in plain text
function saveTable(filename,Obj)
   fd = io.open(filename, 'w')
   fd:write("{\n")
   for k,v in pairs(Obj) do
    fd:write("  ", tostring(k), " = ", tostring(v))
    fd:write(",\n")
   end
   fd:write("}\n")
   fd:close()
end


-- calculate table lengh in lua
function tablelength(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end
