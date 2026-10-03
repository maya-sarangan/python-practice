#!/usr/bin/env bash
# PostToolUse hook: verify the answer key whenever checks/ or solutions/ changes.
#
# Reads the Claude Code hook payload on stdin, pulls out the edited file, and
# runs `python3 practice.py check` if that file lives in checks/ or solutions/.
# Exits 2 on failure so the model is told to fix it rather than moving on.
#
# Test it by hand:
#   echo '{"tool_input":{"file_path":"/abs/path/checks/world1.py"}}' | tools/gate_hook.sh

set -uo pipefail

payload="$(cat)"
file="$(printf '%s' "$payload" \
  | jq -r '.tool_input.file_path // .tool_response.filePath // empty' 2>/dev/null)"

case "$file" in
  */checks/*|*/solutions/*|*/quests/*) ;;
  *) exit 0 ;;
esac

root="$(cd "$(dirname "$file")/.." 2>/dev/null && pwd)" || exit 0
[ -f "$root/practice.py" ] || exit 0

output="$(cd "$root" && python3 practice.py check 2>&1)"
status=$?

if [ "$status" -ne 0 ]; then
  {
    echo "The quest answer key is broken. Fix this before doing anything else."
    echo "Decide whether the CHECK or the SOLUTION is wrong -- do not just bend"
    echo "the check to match a buggy solution."
    echo
    echo "$output"
  } >&2
  exit 2
fi

printf '%s\n' "$output" | tail -n 2
exit 0
