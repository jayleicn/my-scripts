-- File I/O
function readJson(file)
    local cjson = require 'cjson';
    local f = io.open(file, "rb")
    local content = f:read("*all")
    f:close()
    return cjson.decode(content)
end



-- calculate table lengh in lua
function tablelength(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end
