
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONException;

public class re {

    private static final String API_URL_BASE = "http://food2fork.com/api/";
    private static final String API_KEY = "f0b803191090a92dc4309004321efcba";
    private static final OkHttpClient client = new OkHttpClient();

    /**
     * Performs an HTTP GET and parses the response body as JSON.
     */
    private static JSONObject run(String url) throws IOException, JSONException {
        final Request request = new Request.Builder().url(url).build();
        final Response response = client.newCall(request).execute();
        return new JSONObject(response.body().string());
    }

    public static JSONObject search(String query) throws IOException, JSONException {
        final String url = API_URL_BASE + "/search?key=" + API_KEY + "&q=" + URLEncoder.encode(query, "UTF-8");
        return run(url);
    }

    /**
     * Extracts recipe IDs from search results.
     */
    public static List<String> getRecipeIds(JSONObject result) throws IOException, JSONException {
        final ArrayList<String> recipeIds = new ArrayList();
        final JSONArray recipes = result.getJSONArray("recipes");
        for (int i = 0; i < recipes.length(); ++i) {
            final JSONObject recipe = recipes.getJSONObject(i);
            final String id = recipe.getString("recipe_id");
            recipeIds.add(id);
        }
        return recipeIds;
    }

    public static JSONObject getRecipe(String id) throws IOException, JSONException {
        final String url = API_URL_BASE + "get?key=" + API_KEY + "&rId=" + id;
        return run(url);
    }

    public static void main(String[] args) throws JSONException {
        try {
            final JSONObject searchResults = search("shredded chicken");
            // Get and print the first recipe.
            final JSONObject recipe = getRecipe(getRecipeIds(searchResults).get(0));
            System.out.println(recipe.toString(2));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}


