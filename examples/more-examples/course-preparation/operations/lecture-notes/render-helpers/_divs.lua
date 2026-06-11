-- Map pandoc fenced divs to LaTeX tcolorbox environments.
--   ::: board   -> \begin{boardbox} ... \end{boardbox}
--   ::: guess   -> \begin{guessbox} ... \end{guessbox}
-- No-ops for non-LaTeX writers, so the markdown still degrades gracefully.
function Div(el)
  local env
  if el.classes:includes('board') then
    env = 'boardbox'
  elseif el.classes:includes('guess') then
    env = 'guessbox'
  else
    return nil
  end
  local out = { pandoc.RawBlock('latex', '\\begin{' .. env .. '}') }
  for _, b in ipairs(el.content) do out[#out + 1] = b end
  out[#out + 1] = pandoc.RawBlock('latex', '\\end{' .. env .. '}')
  return out
end
