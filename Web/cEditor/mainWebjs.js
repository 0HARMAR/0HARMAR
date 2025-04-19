const { createApp, ref, onMounted } = Vue;

createApp({
    setup() {
        const selectedCompiler = ref('gcc');
        const compileOutput = ref('');
        const disassembly = ref('');
        const isDebugging = ref(false);
        const activeTab = ref('output');
        const registerState = ref('');
        const memoryState = ref('');
        const editor = ref(null);
        const editorContainer = ref(null);

        const tabs = [
            { id: 'output', label: '输出' },
            { id: 'asm', label: '反汇编' },
            { id: 'debug', label: '调试' },
        ];

        onMounted(() => {
            // 配置Monaco Editor
            require.config({ paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.36.1/min/vs' }});
            
            require(['vs/editor/editor.main'], function() {
                editor.value = monaco.editor.create(editorContainer.value, {
                    value: '// 输入C代码...\n#include <stdio.h>\n\nint main() {\n    printf("Hello World!");\n    return 0;\n}',
                    language: 'c',
                    theme: 'vs-dark',
                    minimap: {
                        enabled: false
                    },
                    automaticLayout: true
                });
            });
        });

        const compile = async () => {
            compileOutput.value = '编译中...';
            setTimeout(() => {
                compileOutput.value = 'Hello World!';
                disassembly.value = `00000000 <main>:
  0:   55                      push   ebp
  1:   89 e5                   mov    ebp,esp
  3:   83 ec 10                sub    esp,0x10
  ...`;
            }, 1000);
        };

        const startDebugging = () => {
            isDebugging.value = true;
            activeTab.value = 'debug';
        };

        const stepOver = () => {
            // 调试步过逻辑
        };

        const stepInto = () => {
            // 调试步入逻辑
        };

        const continueExecution = () => {
            // 继续执行逻辑
        };

        return {
            selectedCompiler,
            compileOutput,
            disassembly,
            isDebugging,
            activeTab,
            registerState,
            memoryState,
            tabs,
            editorContainer,
            compile,
            startDebugging,
            stepOver,
            stepInto,
            continueExecution
        };
    }
}).mount('#mainWeb');