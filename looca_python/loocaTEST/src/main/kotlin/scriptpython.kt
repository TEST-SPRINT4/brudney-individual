import java.io.File

class ScriptPython {

    fun execScript() {
        val execPython = "main.py"
        val pythonScriptFile = File(execPython)

        if (!pythonScriptFile.exists()) {
            println("O arquivo $execPython não foi encontrado.")
            return
        }

        try {
            Runtime.getRuntime().exec("py $pythonScriptFile")
        } catch (e: Exception) {
            println("Erro ao executar o script Python: ${e.message}")
        }
    }
}