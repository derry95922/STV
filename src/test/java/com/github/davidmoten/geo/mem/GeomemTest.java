package com.github.davidmoten.geo.mem;

import com.google.common.base.Optional;
import com.google.common.base.Predicate;
import com.google.common.collect.Lists;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class GeomemTest {

    private static final double topLeftLat = 0;
    private static final double topLeftLong = 0;
    private static final double bottomRightLat = -100;
    private static final double bottomRightLong = 100;

    private final double lat = -50;
    private final double lon = 50;
    private final int time = 1;
    private final String value = "d";
    private Optional<String> optional = Optional.of("d"),id;

    Geomem<String,String>geomem;
    Info<String,String>info,testID;
    @Before
    public void setUp() throws Exception {
        geomem = new Geomem<String, String>();
        info = new Info<String, String>(lat,lon,time,value,optional);
        id = Optional.of(value) ;
        testID = new Info<String, String>(lat,lon,time,value,id);
    }

    @Test
    public void find() {
    }

    @Test
    public void createRegionFilter() {
        Geomem<String, String> g = new Geomem<String, String>();
        Predicate<Info<String, String>> predicate = g.createRegionFilter(topLeftLat, topLeftLong, bottomRightLat, bottomRightLong);
        {
            // inside
            assertTrue(predicate.apply(testPoint(topLeftLat -1, topLeftLong +1)));
            // outside north
            assertFalse(predicate.apply(testPoint(topLeftLat + 1, topLeftLong)));
            // outside west
            assertFalse(predicate.apply(testPoint(topLeftLat, topLeftLong - 1)));
            // outside east
            assertFalse(predicate.apply(testPoint(topLeftLat , bottomRightLong + 1)));
            // outside south
            assertFalse(predicate.apply(testPoint(bottomRightLat -1, bottomRightLong )));
        }
    }

    private  Info<String, String> testPoint(double lat, double lon) {
        return new Info<String, String>(lat, lon, 100, "d", Optional.of("d"));
    }

    @Test
    public void add() {
        geomem.add(info);
        Iterable<Info<String,String>>it = geomem.find(0,0,-100,100,0,100);
        assertEquals(info,it.iterator().next());
    }

    @Test
    public void add1() {
        geomem.add(lat,lon,time,value);
        Iterable<Info<String,String>>it = geomem.find(0,0,-100,100,0,100);
        Info<String,String>actual = it.iterator().next();
        assertEquals(info.lat(),actual.lat(),0.1);
        assertEquals(info.lon(),actual.lon(),0.1);
        assertEquals(info.time(),actual.time());
        assertEquals(info.value(),actual.value());
    }

    @Test
    public void add2() {
        geomem.add(lat,lon,time,value,value);
        Iterable<Info<String,String>>it = geomem.find(0,0,-100,100,0,100);
        Info<String,String>actual = it.iterator().next();
        assertEquals(testID.lat(),actual.lat(),0.1);
        assertEquals(testID.lon(),actual.lon(),0.1);
        assertEquals(testID.time(),actual.time());
        assertEquals(testID.value(),actual.value());
        assertEquals(testID.id(),actual.id());

    }

    @Test
    public void add3() {
        geomem.add(lat,lon,time,value,id);
        Iterable<Info<String,String>>it = geomem.find(0,0,-100,100,0,100);
        Info<String,String>actual = it.iterator().next();
        assertEquals(testID.lat(),actual.lat(),0.1);
        assertEquals(testID.lon(),actual.lon(),0.1);
        assertEquals(testID.time(),actual.time());
        assertEquals(testID.value(),actual.value());
        assertEquals(testID.id(),actual.id());

    }
}