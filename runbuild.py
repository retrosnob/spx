from sphinx.cmd.build import main
import sys
import os

def build_sphinx_docs():
    result = main(['-b', 'html', 'source', 'docs'])
    
    if result == 0:
        print("✅ Documentation built successfully!")
        # Ensure .nojekyll exists
        with open('docs/.nojekyll', 'w') as f:
            pass
    else:
        print("❌ Failed to build documentation.", file=sys.stderr)
        sys.exit(result)

if __name__ == '__main__':
    build_sphinx_docs()
