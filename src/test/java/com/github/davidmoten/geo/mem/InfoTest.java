package com.github.davidmoten.geo.mem;

import com.github.davidmoten.geo.GeoHash;
import com.google.common.base.Optional;
import com.google.common.collect.Lists;
import org.junit.Before;
import org.junit.Test;

import java.util.List;

import static org.junit.Assert.*;

public class InfoTest {


    final double lat = 1.5;
    final double lon = 1.5;
    final int time = 1;
    final String value = "d";
    Optional<String>optional =Optional.of(value);
    final double PRECISION = 0.00001;

    Info<String,String>info;
    List<Info<String, String>> list;
    @Before
    public void setUp() throws Exception {
        info = new Info<String, String>(lat,lon,time,value, optional);
        list=Lists.newArrayList();
        list.add(info);
    }

    @Test
    public void id() {
        assertTrue(list.get(0).id().isPresent());
        // get coverage of toString
    }

    @Test
    public void lat() {
        assertEquals(1.5, list.get(0).lat(), PRECISION);
    }

    @Test
    public void lon() {
        assertEquals(1.5, list.get(0).lon(), PRECISION);
    }

    @Test
    public void time() {
        assertEquals(1, list.get(0).time());
    }

    @Test
    public void value() {
        assertEquals("d", list.get(0).value());
    }

    @Test
    public void testToString() {
        assertEquals("Info [lat=" + lat + ", lon=" + lon + ", time="+ time + ", value=" + value + ", id=" + optional + "]",list.get(0).toString());
    }
}